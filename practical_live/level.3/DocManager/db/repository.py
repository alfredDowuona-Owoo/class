# to insert into the db we need connect to the db
from db.database import get_connection
from core.models import Document

class DocumentRepository:
    def add_document(self, doc: Document):
        conn = get_connection()
        cursor = conn.cursor()
    
        cursor.execute("""
        INSERT INTO documents (
        name, path, thumbnail_path, tags, description,
        upload_date,  lecture_date,  total_pages              
        )
        VALUES (?, ?, ?, ?, ?, ?, ?,?)
        """, (
                doc.name,           ## use doc[0] 
                doc.path,           ## use doc[1] 
                doc.thumbnail_path, ## use doc[2] 
                doc.tags,           ## use doc[3] 
                doc.description,    ## use doc[4] 
                doc.upload_date,    ## use doc[5] 
                doc.lecture_date,   ## use doc[6] 
                doc.total_pages     ## use doc[7] 
            ))
        conn.commit()
        conn.close()

    def search_documents(self, tag=None, date =None):
        conn = get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM documents"
        conditions = []
        params = []

        if tag:
            conditions.append("tags LIKE ?")
            params.append(f"%{tag}%")

        if date:
            conditions.append("lecture_date=  ?")
            params.append(date)

        if conditions:
            # last_part_query = " OR ".join(conditions)
            # query+= " WHERE " 
            # query+= last_part_query

            query += " WHERE "+ " OR ".join(conditions)

        cursor.execute(query,params)
        rows=cursor.fetchall()
        conn.close()

        return [Document(*rows) for row in rows]