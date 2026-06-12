from sqlalchemy.orm import Session

from app.models.project import Project

from app.schemas.project import (
    ProjectCreate
)

def create_project(
    db: Session,
    payload: ProjectCreate
):

    project = Project(
        name=payload.name,
        ecosystem=payload.ecosystem,
        funding=payload.funding,
        status=payload.status,
        website=payload.website,
        twitter=payload.twitter
    )

    db.add(project)

    db.commit()

    db.refresh(project)

    return project


def get_projects(
    db: Session
):

    return db.query(
        Project
    ).all()

def search_projects(
    db,
    name=None,
    ecosystem=None,
    status=None
):
    query = db.query(Project)

    if name:
        query = query.filter(
            Project.name.contains(name)
        )

    if ecosystem:
        query = query.filter(
            Project.ecosystem == ecosystem
        )

    if status:
        query = query.filter(
            Project.status == status
        )

    return query.all()

def get_project_by_id(
    db,
    project_id: int
):
    return db.query(
        Project
    ).filter(
        Project.id == project_id
    ).first()

def get_project_stats(db):

    projects = db.query(
        Project
    ).all()

    total = len(projects)

    testnet = len([
        p for p in projects
        if p.status == "Testnet"
    ])

    mainnet = len([
        p for p in projects
        if p.status == "Mainnet"
    ])

    ethereum = len([
        p for p in projects
        if p.ecosystem == "Ethereum"
    ])

    return {
        "total_projects": total,
        "testnet_projects": testnet,
        "mainnet_projects": mainnet,
        "ethereum_projects": ethereum
    }