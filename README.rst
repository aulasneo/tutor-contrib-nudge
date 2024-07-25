nudge plugin for `Tutor <https://docs.tutor.overhang.io>`_
==========================================================

Plugin to enable nudge and highlights emails.

It creates a CronJob in K8s based on the openedx docker image that calls
the `send_course_update` and `send_recurring_nudge` management commands



Installation
------------

::

    pip install git+https://github.com/aulasneo/tutor-contrib-nudge

Configuration
-------------

- NUDGE_SCHEDULE: Set the schedule for the nudge emails. Default is "0 10 \* \* \*" (everyday at 10am).
- NUDGE_SEND_COURSE_UPDATE: Enable course updates. Default is True.
- NUDGE_SEND_RECURRING_NUDGE: Enable recurring nudges. Default is True.


Usage
-----

::

    tutor plugins enable nudge


License
-------

This software is licensed under the terms of the AGPLv3.