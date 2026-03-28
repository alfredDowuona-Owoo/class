# to insert into the db we need connect to the db
from db.database import get_connection

class DocumentRepository:
    def add_document(self, doc):
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