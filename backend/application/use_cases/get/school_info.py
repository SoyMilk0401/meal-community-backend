from backend.application.exceptions import SchoolInfoNotFound
from backend.domain.repositories.school_info import SchoolInfoRepository


class GetSchoolInfoUseCase:
    def __init__(self, school_info_repository: SchoolInfoRepository) -> None:
        self._school_info_repository = school_info_repository

    async def execute(
        self, edu_office_code: str, standard_school_code: str
    ) -> int:
        school_info_id = await self._school_info_repository.get_id_by_code(
            edu_office_code=edu_office_code,
            standard_school_code=standard_school_code,
        )
        
        if not school_info_id:
            raise SchoolInfoNotFound
        
        return school_info_id