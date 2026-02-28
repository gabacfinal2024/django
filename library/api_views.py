"""
JSON API for Thunder Client / REST clients: List (Read), Create, Delete.
"""
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Author, Book, Member, Loan


def _serialize_author(a):
    return {"id": a.pk, "name": a.name, "email": a.email}


def _serialize_book(b):
    return {
        "id": b.pk,
        "title": b.title,
        "isbn": b.isbn,
        "author_id": b.author_id,
        "author_name": b.author.name,
        "published": b.published.isoformat() if b.published else None,
    }


def _serialize_member(m):
    return {
        "id": m.pk,
        "name": m.name,
        "email": m.email,
        "phone": m.phone or "",
        "join_date": m.join_date.isoformat(),
    }


def _serialize_loan(l):
    return {
        "id": l.pk,
        "book_id": l.book_id,
        "book_title": l.book.title,
        "member_id": l.member_id,
        "member_name": l.member.name,
        "loan_date": l.loan_date.isoformat(),
        "due_date": l.due_date.isoformat(),
        "return_date": l.return_date.isoformat() if l.return_date else None,
    }


# ----- Authors API -----
@require_http_methods(["GET"])
def api_author_list(request):
    authors = list(Author.objects.all().values("id", "name", "email"))
    return JsonResponse({"authors": authors})


@csrf_exempt
@require_http_methods(["POST"])
def api_author_create(request):
    try:
        data = json.loads(request.body) if request.body else {}
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    name = data.get("name")
    email = data.get("email")
    if not name or not email:
        return JsonResponse({"error": "name and email required"}, status=400)
    author = Author.objects.create(name=name, email=email)
    return JsonResponse(_serialize_author(author), status=201)


@csrf_exempt
@require_http_methods(["DELETE"])
def api_author_delete(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)
    author.delete()
    return JsonResponse({"ok": True})


# ----- Books API -----
@require_http_methods(["GET"])
def api_book_list(request):
    books = []
    for b in Book.objects.select_related("author").all():
        books.append(_serialize_book(b))
    return JsonResponse({"books": books})


@csrf_exempt
@require_http_methods(["POST"])
def api_book_create(request):
    try:
        data = json.loads(request.body) if request.body else {}
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    title = data.get("title")
    isbn = data.get("isbn")
    author_id = data.get("author_id")
    published = data.get("published")
    if not title or not isbn or not author_id:
        return JsonResponse({"error": "title, isbn, author_id required"}, status=400)
    if not Author.objects.filter(pk=author_id).exists():
        return JsonResponse({"error": "author_id not found"}, status=400)
    book = Book.objects.create(
        title=title,
        isbn=isbn,
        author_id=author_id,
        published=published or None,
    )
    return JsonResponse(_serialize_book(book), status=201)


@csrf_exempt
@require_http_methods(["DELETE"])
def api_book_delete(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)
    book.delete()
    return JsonResponse({"ok": True})


# ----- Members API -----
@require_http_methods(["GET"])
def api_member_list(request):
    members = list(
        Member.objects.all().values("id", "name", "email", "phone", "join_date")
    )
    for m in members:
        m["join_date"] = m["join_date"].isoformat()
    return JsonResponse({"members": members})


@csrf_exempt
@require_http_methods(["POST"])
def api_member_create(request):
    try:
        data = json.loads(request.body) if request.body else {}
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    name = data.get("name")
    email = data.get("email")
    join_date = data.get("join_date")
    if not name or not email or not join_date:
        return JsonResponse({"error": "name, email, join_date required"}, status=400)
    member = Member.objects.create(
        name=name,
        email=email,
        phone=data.get("phone", ""),
        join_date=join_date,
    )
    return JsonResponse(_serialize_member(member), status=201)


@csrf_exempt
@require_http_methods(["DELETE"])
def api_member_delete(request, pk):
    try:
        member = Member.objects.get(pk=pk)
    except Member.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)
    member.delete()
    return JsonResponse({"ok": True})


# ----- Loans API -----
@require_http_methods(["GET"])
def api_loan_list(request):
    loans = []
    for l in Loan.objects.select_related("book", "member").all():
        loans.append(_serialize_loan(l))
    return JsonResponse({"loans": loans})


@csrf_exempt
@require_http_methods(["POST"])
def api_loan_create(request):
    try:
        data = json.loads(request.body) if request.body else {}
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    book_id = data.get("book_id")
    member_id = data.get("member_id")
    loan_date = data.get("loan_date")
    due_date = data.get("due_date")
    if not all([book_id, member_id, loan_date, due_date]):
        return JsonResponse(
            {"error": "book_id, member_id, loan_date, due_date required"}, status=400
        )
    try:
        loan = Loan.objects.create(
            book_id=book_id,
            member_id=member_id,
            loan_date=loan_date,
            due_date=due_date,
            return_date=data.get("return_date") or None,
        )
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse(_serialize_loan(loan), status=201)


@csrf_exempt
@require_http_methods(["DELETE"])
def api_loan_delete(request, pk):
    try:
        loan = Loan.objects.get(pk=pk)
    except Loan.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)
    loan.delete()
    return JsonResponse({"ok": True})
