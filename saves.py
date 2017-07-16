import json
import ocObjects

projects    = []
actions     = []
events      = []
inbox       = []
tags        = []

due_soon     = []
over_due     = []

sorting_key_a = 'title'
sorting_key_i = 'title'
sorting_key_p = 'title'


def sort_actions(sorting_key):
    global sorting_key_a
    sorting_key_a = sorting_key

    if sorting_key == 'comment':
        return sorted(actions, key=lambda a: a.comment)
    elif sorting_key == 'date_added':
        return sorted(actions, key=lambda a: a.date_added)
    elif sorting_key == 'date_changed':
        return sorted(actions, key=lambda a: a.date_changed)
    elif sorting_key == 'defer_until':
        return sorted(actions, key=lambda a: a.defer_until)
    elif sorting_key == 'display_index':
        return sorted(actions, key=lambda a: a.display_index)
    elif sorting_key == 'due':
        return sorted(actions, key=lambda a: a.due)
    elif sorting_key == 'est_time':
        return sorted(actions, key=lambda a: a.est_time)
    elif sorting_key == 'flagged':
        return sorted(actions, key=lambda a: a.flagged)
    elif sorting_key == 'project':
        return sorted(actions, key=lambda a: a.project)
    elif sorting_key == 'status':
        return sorted(actions, key=lambda a: a.status)
    elif sorting_key == 'tags':
        return sorted(actions, key=lambda a: a.tags)
    elif sorting_key == 'title':
        return sorted(actions, key=lambda a: a.title)


def sort_inbox(sorting_key):
    global sorting_key_i
    sorting_key_i = sorting_key

    if sorting_key == 'comment':
        return sorted(actions, key=lambda i: i.comment)
    elif sorting_key == 'date_added':
        return sorted(actions, key=lambda i: i.date_added)
    elif sorting_key == 'date_changed':
        return sorted(actions, key=lambda i: i.date_changed)
    elif sorting_key == 'defer_until':
        return sorted(actions, key=lambda i: i.defer_until)
    elif sorting_key == 'display_index':
        return sorted(actions, key=lambda i: i.display_index)
    elif sorting_key == 'due':
        return sorted(actions, key=lambda i: i.due)
    elif sorting_key == 'est_time':
        return sorted(actions, key=lambda i: i.est_time)
    elif sorting_key == 'flagged':
        return sorted(actions, key=lambda i: i.flagged)
    elif sorting_key == 'status':
        return sorted(actions, key=lambda i: i.status)
    elif sorting_key == 'tags':
        return sorted(actions, key=lambda i: i.tags)
    elif sorting_key == 'title':
        return sorted(actions, key=lambda i: i.title)


def sort_projects(sorting_key):
    global sorting_key_p
    sorting_key_p = sorting_key

    if sorting_key == 'comment':
        return sorted(projects, key=lambda p: p.comment)
    elif sorting_key == 'date_added':
        return sorted(projects, key=lambda p: p.date_added)
    elif sorting_key == 'date_changed':
        return sorted(projects, key=lambda p: p.date_changed)
    elif sorting_key == 'defer_until':
        return sorted(projects, key=lambda p: p.defer_until)
    elif sorting_key == 'display_index':
        return sorted(projects, key=lambda p: p.display_index)
    elif sorting_key == 'due':
        return sorted(projects, key=lambda p: p.due)
    elif sorting_key == 'est_time':
        return sorted(projects, key=lambda p: p.est_time)
    elif sorting_key == 'flagged':
        return sorted(projects, key=lambda p: p.flagged)
    elif sorting_key == 'status':
        return sorted(projects, key=lambda p: p.status)
    elif sorting_key == 'tags':
        return sorted(projects, key=lambda p: p.tags)
    elif sorting_key == 'title':
        return sorted(projects, key=lambda p: p.title)


def list_to_file(filename):

    fp = open(filename, 'r+')

    fp.truncate()

    if filename == 'actions.txt':
        all_data = []
        for a in actions:
            action_data = []
            for d in [a.comment,
                      a.date_added,
                      a.date_changed,
                      a.defer_until,
                      a.display_index,
                      a.due,
                      a.est_time,
                      a.flagged,
                      a.project,
                      a.status,
                      a.tags,
                      a.title
                      ]:
                action_data.append(d)
            all_data.append(action_data)
        json.dump(all_data, fp)

    elif filename == 'events.txt':
        all_data = []
        for e in events:
            event_data = []
            for d in [e.comment,
                      e.date_start,
                      e.date_end,
                      e.project,
                      e.tags,
                      e.title
                      ]:
                event_data.append(d)
            all_data.append(event_data)
        json.dump(all_data, fp)

    elif filename == 'inbox.txt':
        all_data = []
        for i in inbox:
            inbox_data = []
            for d in [i.comment,
                      i.date_added,
                      i.date_changed,
                      i.defer_until,
                      i.display_index,
                      i.due,
                      i.est_time,
                      i.flagged,
                      i.project,
                      i.status,
                      i.tags,
                      i.title]:
                inbox_data.append(d)
            all_data.append(inbox_data)
        json.dump(all_data, fp)

    elif filename == 'projects.txt':
        all_data = []
        for p in projects:
            project_data = []
            for d in [p.comment,
                      p.date_added,
                      p.date_changed,
                      p.defer_until,
                      p.display_index,
                      p.due,
                      p.est_time,
                      p.flagged,
                      p.status,
                      p.tags,
                      p.title]:
                project_data.append(d)
            all_data.append(project_data)
        json.dump(all_data, fp)

    elif filename == 'tags.txt':
        json.dump(tags, fp)

    else:
        print('ERROR in saves.py: Wrong \'filename\' passed to list_to_file() method')


def file_to_list(filename):

    fp = open(filename, 'r')
    json_string = fp.read()

    if len(json_string) == 0:

        # file is empty, json module cannot load it -> leave list as it is
        pass

    elif len(json_string) != 0:

        if filename == 'actions.txt':

            all_data = json.loads(json_string)
            global actions
            actions = []

            for d in all_data:

                a = ocObjects.Action()

                a.comment       = d[0]
                a.dateAdded     = d[1]
                a.dateChanged   = d[2]
                a.deferUntil    = d[3]
                a.displayIndex  = d[4]
                a.due           = d[5]
                a.estTime       = d[6]
                a.flagged       = d[7]
                a.project       = d[8]
                a.status        = d[9]
                a.tags          = d[10]
                a.title         = d[11]

                actions.append(a)

        elif filename == 'events.txt':

            all_data = json.loads(json_string)
            global events
            events = []

            for d in all_data:
                e = ocObjects.Event()

                e.comment       = d[0]
                e.dateStart     = d[1]
                e.dateEnd       = d[2]
                e.project       = d[3]
                e.tags          = d[4]
                e.title         = d[5]

                events.append(e)

        elif filename == 'inbox.txt':

            all_data = json.loads(json_string)
            global inbox
            inbox = []

            for d in all_data:
                a = ocObjects.Action()

                a.comment       = d[0]
                a.dateAdded     = d[1]
                a.dateChanged   = d[2]
                a.deferUntil    = d[3]
                a.displayIndex  = d[4]
                a.due           = d[5]
                a.estTime       = d[6]
                a.flagged       = d[7]
                a.project       = d[8]
                a.status        = d[9]
                a.tags          = d[10]
                a.title         = d[11]

                inbox.append(a)

        elif filename == 'projects.txt':

            all_data = json.loads(json_string)
            global projects
            projects = []

            for d in all_data:

                p = ocObjects.Project()

                p.comment       = d[0]
                p.dateAdded     = d[1]
                p.dateChanged   = d[2]
                p.deferUntil    = d[3]
                p.displayIndex  = d[4]
                p.due           = d[5]
                p.estTime       = d[6]
                p.flagged       = d[7]
                p.status        = d[8]
                p.tags          = d[9]
                p.title         = d[10]

                projects.append(p)


        elif filename == 'tags.txt':

            global tags
            tags = json.loads(json_string)


        else:
            print('ERROR in saves.py: Wrong \'filename\' passed to file_to_list() method')

    else:
        print('This shouldn\'t happen. (else-statement in saves.file_to_ist())')

        fp.close()
"""
p1 = ocObjects.Project()
p1.title = 'Learn to solve a Rubix Cube'
p1.flagged = True
projects.append(p1)

p2 = ocObjects.Project()
p2.title = 'PEP2'
p2.flagged = False
projects.append(p2)

p3 = ocObjects.Project()
p3.title = 'PTP2'
p3.flagged = False
projects.append(p3)

list_to_file('projects.txt')
"""
