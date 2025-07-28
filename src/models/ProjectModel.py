from .BaseDataModel import BaseDataModel
from .db_schemes.project import Project
from .enums.DataBaseEnums import DataBaseEnums

class ProjectModel(BaseDataModel):
    def __init__(self, db_cilent: object):
        super().__init__(db_client=db_cilent)
        self.collection = self.db_client[DataBaseEnums.COLLECTION_PROJECT_NAME.value]
    
    async def create_project(self, project: Project):
        result = await self.collection.insert_one(Project.dict())
        project.id = result.inserted_id

        return project

    async def get_project_or_create_one(self, project_id: str):
        record = await self.collection.find_one({
            "project_id": project_id
        })

        if record in None:
            # create new project
            project = Project(project_id=project_id)
            project = await self.create_project(project)
            
            return project
        
        return Project(**record)
    
    async def get_all_projects(self, page: int=1, page_size: int=10):
        # count total number of documents in db
        total_documents = await self.collection.count_documents({})

        # calculate total number of pages
        total_pages = total_documents // page_size
        if total_documents % page_size > 0:
            total_pages += 1

        cursor = self.collection.find().skip( (page-1) * page_size ).limit(page_size)
        projects = []
        async for document in cursor:
            projects.append(
                Project(**document)
            )

        return projects, total_pages

