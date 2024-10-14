"""DB module provides sqliite DB data dump capabilities."""

# Standard library imports
from __future__ import annotations
import sqlite3
import logging

# Local library imports
from med_crawler.parser.parser import (
        Entry,
        Pos,
        Etymology,
        Form,
        Sense,
        Citation,
)


logger = logging.Logger(__name__)


class SqliteMedDbException(Exception):
    """SqliteMedDbException"""


class SqliteMedDbInsertException(SqliteMedDbException):
    """SqliteMedDbInsertException"""


class SqliteMedDB:

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def __enter__(self) -> SqliteMedDB:
        try:
            self.conn = sqlite3.connect(self.file_name)
        except Exception as err:
            logger.error(f"Sqlite DB error: {err}")
            raise SqliteMedDbException(err) from err
        return self

    def __exit__(self, exc_type, exc_val, traceback) -> None:
        self.conn.close()

    def create_tables(self) -> None:
        for create_table in (
           self._create_lemma_table,
           self._create_pos_table,
           self._create_etymology_table,
           self._create_form_table,
           self._create_sense_table,
           self._create_citation_table,
        ):
            try:
                create_table()
            except sqlite3.OperationalError as err:
                logger.error(f"Sqlite DB error: {err}")
                self.conn.rollback()
                return
            self.conn.commit()

    def _create_lemma_table(self) -> None:
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE entry (
                id TEXT PRIMARY KEY,
                source_id TEXT NOT NULL,
                lemma_regular TEXT NOT NULL,
                lemma_original TEXT NOT NULL
            );
            """
        )
        cur.execute(
            "CREATE UNIQUE INDEX idx_unique_source_id "
            "on entry (source_id);"
        )
        cur.execute(
            "CREATE INDEX idx_unique_lemma_regular "
            "on entry (lemma_regular);"
        )
        cur.close()

    def insert_to_entry_table(self, entry: Entry.DTO) -> None:
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO entry (
                id,
                source_id,
                lemma_regular,
                lemma_original
            ) VALUES (
                :id,
                :source_id,
                :lemma_regular,
                :lemma_original
            );
            """,
            entry,
        )
        self.conn.commit()
        cur.close()

    def _create_pos_table(self) -> None:
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE pos (
                id TEXT PRIMARY KEY,
                entry_id TEXT NOT NULL,
                code TEXT NOT NULL,
                code_abbrev TEXT NULL,
                FOREIGN KEY (entry_id) REFERENCES entry (id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            );
            """
        )
        cur.close()

    def insert_to_pos_table(self, pos: Pos.DTO) -> None:
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO pos (
                id,
                entry_id,
                code,
                code_abbrev
            ) VALUES (
                :id,
                :entry_id,
                :code,
                :code_abbrev
            );
            """,
            pos,
        )
        self.conn.commit()
        cur.close()

    def _create_etymology_table(self) -> None:
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE etymology (
                id TEXT PRIMARY KEY,
                entry_id TEXT NOT NULL,
                code text NOT NULL,
                code_abbrev TEXT NULL,
                FOREIGN KEY (entry_id) REFERENCES entry (id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            );
            """
        )
        cur.close()

    def insert_to_etymology_table(self, etymology: Etymology.DTO) -> None:
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO etymology (
                id,
                entry_id,
                code,
                code_abbrev
            ) VALUES (
                :id,
                :entry_id,
                :code,
                :code_abbrev
            );
            """,
            etymology,
        )
        self.conn.commit()
        cur.close()

    def _create_form_table(self) -> None:
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE form (
                id TEXT PRIMARY KEY,
                entry_id TEXT NOT NULL,
                form_regular TEXT NOT NULL,
                form_original TEXT NOT NULL,
                FOREIGN KEY (entry_id) REFERENCES entry (id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            );
            """
        )
        cur.close()

    def insert_to_form_table(self, form: Form.DTO) -> None:
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO form (
                id,
                entry_id,
                form_regular,
                form_original
            ) VALUES (
                :id,
                :entry_id,
                :form_regular,
                :form_original
            );
            """,
            form,
        )
        self.conn.commit()
        cur.close()

    def _create_sense_table(self) -> None:
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE sense (
                id TEXT PRIMARY KEY,
                entry_id TEXT NOT NULL,
                text TEXT NOT NULL,
                FOREIGN KEY (entry_id) REFERENCES entry (id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            );
            """
        )
        cur.close()

    def insert_to_sense_table(self, sense: Sense.DTO) -> None:
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO sense (
                id,
                entry_id,
                text
            ) VALUES (
                :id,
                :entry_id,
                :text
            );
            """,
            sense,
        )
        self.conn.commit()
        cur.close()

    def _create_citation_table(self) -> None:
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE citation (
                id TEXT PRIMARY KEY,
                entry_id TEXT NOT NULL,
                date TEXT NULL,
                author TEXT NULL,
                title TEXT NULL,
                manuscript TEXT NULL,
                scope TEXT NULL,
                text TEXT NOT NULL,
                reference TEXT NULL,
                FOREIGN KEY (entry_id) REFERENCES entry (id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            );
            """
        )
        cur.close()

    def insert_to_citation_table(self, citation: Citation.DTO) -> None:
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO citation (
                id,
                entry_id,
                date,
                author,
                title,
                manuscript,
                scope,
                text,
                reference
            ) VALUES (
                :id,
                :entry_id,
                :date,
                :author,
                :title,
                :manuscript,
                :scope,
                :text,
                :reference
            );
            """,
            citation,
        )
        self.conn.commit()
        cur.close()
