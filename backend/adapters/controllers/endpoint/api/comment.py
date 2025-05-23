from sanic import json
from sanic.blueprints import Blueprint
from sanic_ext import validate

from backend.application.dtos.comment import CreateCommentDTO
from backend.application.use_cases.create.comment import CreateNewCommentUseCase
from backend.application.use_cases.create.comment import CreateReplyCommentUseCase
from backend.domain.entities.comment import Comment

from backend.application.use_cases.get.user import GetUserByIDUseCase
from backend.application.exceptions import UserNotFound

from backend.infrastructure.jwt import require_auth
from backend.infrastructure.sanic import BackendRequest

comment = Blueprint("comment_endpoint", url_prefix="/comment")

@comment.post("/write")
@validate(json=CreateCommentDTO, body_argument="create_comment_dto")
@require_auth
async def write_comment(
    request: BackendRequest,
    create_comment_dto: CreateCommentDTO,
    user_id: int,
):
    user = await GetUserByIDUseCase(request.app.ctx.user_repository).execute(
       user_id
    )

    comment_entity = Comment(
        content=create_comment_dto.content,
        author=user)
    
    await CreateNewCommentUseCase(request.app.ctx.comment_repository).execute(
            user_id=user_id, 
            meal_id=create_comment_dto.meal_id, 
            comment=comment_entity
        )
        
    return json({"message": "Comment created successfully"})

@comment.post("/reply")
@validate(json=CreateCommentDTO, body_argument="create_comment_dto")
@require_auth
async def write_reply(
    request: BackendRequest,
    create_comment_dto: CreateCommentDTO,
    user_id: int,
):
    if create_comment_dto.parent_id is None:
        return json({"error": "Parent ID is required"})

    user = await GetUserByIDUseCase(request.app.ctx.user_repository).execute(
        user_id
    )

    comment_entity = Comment(
        content=create_comment_dto.content,
        author=user,
        parent_id=create_comment_dto.parent_id)
    
    await CreateReplyCommentUseCase(request.app.ctx.comment_repository).execute(
            user_id=user_id,
            meal_id=create_comment_dto.meal_id, 
            comment=comment_entity,
            parent_comment_id=comment_entity.parent_id
        )
        
    return json({"message": "Reply created successfully"})