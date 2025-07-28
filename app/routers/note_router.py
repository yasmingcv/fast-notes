from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.domain import NoteCreate, NoteUpdate, NoteResponse, UserResponse
from app.services import note_service
from app.auth import get_current_user

router = APIRouter(prefix="/notes", tags=["notes"])

@router.post("/", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
def create_note(
    note: NoteCreate, 
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    print('current_user', current_user)
    if (current_user is None):
        raise HTTPException(status_code=401, detail="User not authenticated")
    try:
        data = NoteCreate(
            content=note.content,
            title=note.title,
            user_id=current_user.id
        )
        print('data', data)
        note = note_service.create(db, data)
        return note
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[NoteResponse])
def list_user_notes(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    try:
        notes = note_service.get_notes_by_user(db, current_user.id, skip, limit)
        return notes
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{note_id}", response_model=NoteResponse)
def get_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    try:
        note = note_service.get_by_id(db, note_id)
        if not note:
            raise HTTPException(status_code=404, detail="Note not found")
        
        if note.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="Access denied: you can only access your own notes")
        
        return note
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{note_id}", response_model=NoteResponse)
def update_note(
    note_id: int,
    note_update: NoteUpdate,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    try:
        existing_note = note_service.get_by_id(db, note_id)
        if not existing_note:
            raise HTTPException(status_code=404, detail="Note not found")
        
        if existing_note.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="Access denied: you can only update your own notes")
        
        updated_note = note_service.update(db, note_id, note_update)
        if not updated_note:
            raise HTTPException(status_code=404, detail="Error updating note")
        
        return updated_note
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    try:
        existing_note = note_service.get_by_id(db, note_id)
        if not existing_note:
            raise HTTPException(status_code=404, detail="Note not found")
        
        if existing_note.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="Access denied: you can only delete your own notes")
        
        success = note_service.delete(db, note_id)
        if not success:
            raise HTTPException(status_code=404, detail="Error deleting note")
        
        return None
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
