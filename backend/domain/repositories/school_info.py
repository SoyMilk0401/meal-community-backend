from abc import ABC, abstractmethod

from backend.domain.entities.school import School


class SchoolInfoRepository(ABC):
    @abstractmethod
    async def get_by_name(self, name: str) -> list[School]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_code(
        self, edu_office_code: str, standard_school_code: str
    ) -> School | None:
        raise NotImplementedError
    
    @abstractmethod
    async def get_id_by_code(
        self, edu_office_code: str, standard_school_code: str
    ) -> int | None:
        raise NotImplementedError