from abc import ABC, abstractmethod

from backend.domain.entities.school_info import SchoolInfo


class SchoolInfoRepository(ABC):

    @abstractmethod
    async def get_by_code(
        self, edu_office_code: str, standard_school_code: str
    ) -> SchoolInfo | None:
        raise NotImplementedError

    @abstractmethod
    async def get_id_by_code(
        self, edu_office_code: str, standard_school_code: str
    ) -> int | None:
        raise NotImplementedError
