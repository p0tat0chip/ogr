import datetime
from typing import Any
from pyforgejo.types.comment import Comment as FComment
from ogr.abstract import Comment, IssueComment, PRComment

class ForgejoComment(Comment):
    def _from_raw_comment(self, raw_comment: FComment) -> None:
        self._raw_comment = raw_comment

    @property
    def body(self) -> str:
        return self._raw_comment.body

    @property
    def edited(self) -> datetime.datetime:
        return self._raw_comment.updated_at
    
class ForgejoIssueComment(ForgejoComment, IssueComment):
    def __str__(self):
        return "Forgejo" + super().__str__()

class ForgejoPRComment(ForgejoComment, PRComment):
    def __str__(self):
        return "Forgejo" + super().__str__()
