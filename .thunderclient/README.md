# Thunder Client – Library API

## Import the collection

1. **Start Django** (in project root):
   ```bash
   .\venv\Scripts\activate
   python manage.py runserver
   ```

2. **In Cursor/VS Code**: install the **Thunder Client** extension if you haven’t.

3. **Import**:
   - Open Thunder Client (sidebar or Command Palette: “Thunder Client”).
   - Click the **Menu** (⋮) on the Collections side.
   - Choose **Import** → **Collection**.
   - Select:  
     `c:\Users\acer\Downloads\django1\.thunderclient\Library-API.postman_collection.json`  
   - Or drag that file into Thunder Client.

4. **Set base URL** (optional):
   - Create an **Environment** in Thunder Client (e.g. “Local”).
   - Add variable: `baseUrl` = `http://127.0.0.1:8000`
   - Select that environment so `{{baseUrl}}` in requests resolves.

5. **Send requests**:
   - **Authors**: List (GET), Create (POST), Delete (DELETE – change `1` in the URL to the author id).
   - **Books**, **Members**, **Loans**: same pattern.  
   For Create, edit the JSON body (e.g. `author_id`, `book_id`, `member_id`, dates) as needed.

## API base

- List (Read): `GET /api/authors/`, `/api/books/`, `/api/members/`, `/api/loans/`
- Create: `POST /api/.../create/` with JSON body.
- Delete: `DELETE /api/.../<id>/delete/`
