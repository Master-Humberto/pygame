.. include:: common.txt

:mod:`pygame.context`
======================

.. module:: pygame.context
    :synopsis: pygame module to provide additional context on the system

| :sl:`pygame module to provide additional context on the system`

.. function:: get_pref_path

   | :sl:`get a writeable folder for your app`
   | :sg:`get_pref_path(org, app) -> path`

   When distributing apps, it's helpful to have a way to get a writeable path,
   because it's what apps are expected to do, and because sometimes the local
   space around the app isn't writeable to the app.

   This function returns a platform specific path for your app to store
   savegames, settings, and the like. This path is unique per user and
   per app name.

   It takes two strings, ``org`` and ``app``. It then will figure out the
   preferred path, creating the folders referenced by the path if necessary,
   and returns an absolute path.

   On Windows, it would be like
   ::
    C:\\Users\\bob\\AppData\\Roaming\\My Company\\My Program Name\\

   On Mac, it would be like
   ::
    /Users/bob/Library/Application Support/My Program Name/
