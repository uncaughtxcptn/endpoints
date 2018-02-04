from aiopg.sa import create_engine

import datetime

import psycopg2

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column, Integer, String, DateTime, ForeignKey, Text)
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable, DropTable


Base = declarative_base()


class Endpoint(Base):
    __tablename__ = 'endpoint'
    id = Column(Integer, primary_key=True)
    hash = Column(String(256), unique=True)
    when = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)

    access_logs = relationship(
        'AccessLog', back_populates='endpoint', cascade='all, delete')
    responses = relationship(
        'Response', back_populates='endpoint', cascade='all, delete')

    def __repr__(self):
        return '<Endpoint(id="{}", hash="")>'.format(self.id, self.hash)


class AccessLog(Base):
    __tablename__ = 'access_log'
    id = Column(Integer, primary_key=True)
    request = Column(Text, default='')
    response = Column(Text, default='')
    endpoint_id = Column(Integer, ForeignKey('endpoint.id'))
    when = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)

    endpoint = relationship('Endpoint', back_populates='access_logs')

    def __repr__(self):
        return '<AccessLog(id="{}", endpoint="{}")>'.format(
            self.id, self.endpoint)


class Response(Base):
    __tablename__ = 'response'
    id = Column(Integer, primary_key=True)
    headers = Column(Text, default='{}')
    status_code = Column(Integer, default=200)
    body = Column(Text, default='')
    endpoint_id = Column(Integer, ForeignKey('endpoint.id'))

    endpoint = relationship('Endpoint', back_populates='responses')

    def __repr__(self):
        return '<Response(id="{}", endpoint="{}")>'.format(
            self.id, self.endpoint)


async def delete_tables(pg, tables):
    async with pg.acquire() as conn:
        for table in reversed(tables):
            drop_expr = DropTable(table)
            try:
                return await conn.execute(drop_expr)
            except psycopg2.ProgrammingError:
                pass


async def prepare_tables(pg):
    tables = [Endpoint.__table__, AccessLog.__table__, Response.__table__]
    # await delete_tables(pg, tables)
    async with pg.acquire() as conn:
        for table in tables:
            try:
                create_expr = CreateTable(table)
                await conn.execute(create_expr)
            except psycopg2.ProgrammingError:
                pass


async def init_pg(app):
    db_conf = app['config']['database']
    engine = await create_engine(
        database=db_conf['name'],
        user=db_conf['user'],
        password=db_conf['password'],
        host=db_conf['host'],
        port=db_conf['port'])
    await prepare_tables(engine)
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()
    del app['db']
