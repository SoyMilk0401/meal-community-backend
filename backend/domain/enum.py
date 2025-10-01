from enum import Enum


class CreateCommentStatus(Enum):
    SUCCESS = "success"
    AUTHOR_NOT_FOUND = "author_not_found"
    PARENT_COMMENT_NOT_FOUND = "parent_comment_not_found"


class CreateMealStatus(Enum):
    SCHOOL_INFO_NOT_FOUND = "school_info_not_found"

class CreateTimetableStatus(Enum):
    SCHOOL_INFO_NOT_FOUND = "school_info_not_found"
    
class CreateRatingStatus(Enum):
    SUCCESS = "success"
    MEAL_INFO_NOT_FOUND = "meal_info_not_found"
    ALREADY_RATED = "already_rated"