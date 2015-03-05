'''
Various constants extracted from schema.

Created on Oct 15, 2013

@author: pupssman
'''
from collections import namedtuple


class Status(object):
    FAILED = 'failed'
    BROKEN = 'broken'
    PASSED = 'passed'
    CANCELED = 'canceled'
    PENDING = 'pending'


class Label(object):
    DEFAULT = 'allure_label'
    FEATURE = 'feature'
    STORY = 'story'
    SEVERITY = 'severity'
    ISSUE = 'issue'


class Severity(object):
    BLOCKER = 'blocker'
    CRITICAL = 'critical'
    NORMAL = 'normal'
    MINOR = 'minor'
    TRIVIAL = 'trivial'


AttachTuple = namedtuple('AttachTuple', ['mime_type', 'extension'])


class AttachmentType(object):
    TEXT = AttachTuple("text/plain", "txt")
    HTML = AttachTuple("application/html", "html")
    XML = AttachTuple("application/xml", "xml")
    PNG = AttachTuple("image/png", "png")
    JPG = AttachTuple("image/jpg", "jpg")
    JSON = AttachTuple("application/json", "json")
    OTHER = AttachTuple("other", "other")


ALLURE_NAMESPACE = "urn:model.allure.qatools.yandex.ru"
COMMON_NAMESPACE = "urn:model.commons.qatools.yandex.ru"
FAILED_STATUSES = [Status.FAILED, Status.BROKEN]
SKIPPED_STATUSES = [Status.CANCELED, Status.PENDING]
