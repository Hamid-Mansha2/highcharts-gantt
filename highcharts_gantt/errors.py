from highcharts_core.errors import *


class AsanaAuthenticationError(HighchartsValueError):
    """:exc:`ValueError <python:ValueError>` encountered when trying to call 
    :meth:`GanttSeries.from_asana() <highcharts_gantt.options.series.gantt.GanttSeries.from_asana>` 
    with improperly configured authentication."""
    pass


class MondayAuthenticationError(HighchartsValueError):
    """:exc:`ValueError <python:ValueError>` encountered when trying to call 
    :meth:`GanttSeries.from_monday() <highcharts_gantt.options.series.gantt.GanttSeries.from_monday>` 
    with improperly configured authentication."""
    pass


class JIRAAuthenticationError(HighchartsValueError):
    """:exc:`ValueError <python:ValueError>` encountered when trying to call 
    :meth:`GanttSeries.from_jira() <highcharts_gantt.options.series.gantt.GanttSeries.from_jira>` 
    with improperly configured authentication."""
    pass


class MondayTemplateError(HighchartsValueError):
    """:exc:`ValueError <python:ValueError>` encountered when attempting to apply a 
    Monday.com template that is not supported by **Highcharts Gantt for Python**.
    """
    pass


class DuplicateJIRAIssueError(HighchartsValueError):
    """:exc:`ValueError <python:ValueError>` encountered when encountering a JIRA issue 
    that is a duplicate of another issue."""
    pass
