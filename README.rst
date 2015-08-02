======================
UPJS: intro to gamedev
======================

* Optional subject (C)
* Goal:
  - Popularize/explain gamedev among the 'mildly interested' (majority at PF UPJS)
  - Allow the informed/hardcore to do more
* Based on student's initiative, with an easy fallback route for students with no
  initiative (**which is expected to be taken by the majority of students**)
  - Easy to pass, credit count low to discourage credit whoring
    (which is unlikely/impractical on PF UPJS already)
* Base concept: Robert Novotny: Softverovy Projekt
* Series of independent 'topic talks' rather than 'a subject',
  with a game project at the background
* Projects proposed *by students* (but low minimum requirements)
* All content available online (slides, tutorials, source code)
* I like bullet points


**Everything is very early and can change, feel free to send pull requests with changes to anything**


---------------
Near-term TODO:
---------------

* A service that downloads topic slides and builds them/puts them online 
  every time they are modified
* Topic slides for at least 2 different non-intro topics
* Complete draft of the intro topic

------
Topics
------

* If no time to flesh out a topic, add an idea to `TopicIdeas.rst <https://github.com/kiith-sa/upjs-gamedev/blob/master/CHANGES.rst>`_
* A topic (e.g. financing, level design) should have the scope of a single talk.
* Should be independent so they can be presented in any order.
* High-level, with references/links to in-depth resources.
* Should *not* be authoritative (e.g. "this is the way X is done", "you must do A, B and C"),
  but rather, "we do X this way because A", "people in K sub-industry do X that way
  because B is more important to them than A"

  - everyone does things differently, it's not just AAA/indie/mobile/whatever
* There may be any number of topics, some of them will be picked over a semester
* Every topic will specify video/s or image/s thet can be shown at the end of
  the *preciding talk*: "next time on <subject name>"


---------------------------
Editing/adding topic slides
---------------------------

* Create a new subdirectory named `$topic` in `topics/`, where `$topic` is the name of the
  topic.
* Copy the `slides/` subdirectory from some other topic to `topics/$topic`
  (e.g. `topics/intro/slides` to `topics/$topic/slides`).
* Edit files in `topics/$topic/slides/source`, particularly
  `index.rst` (with a text editor). A slide looks
  like this (**but really, just copy and paste and edit**)::

     ----------------
     Slide title here
     ----------------

     * Point 1
     * Point 2

       - **Bold** *italic* ``monospace`` subpoint 2.1
     * Point 3

       This is a centered image with 90% width of the slide in file
       `topics/$topic/slides/source/image.png`

       .. figure:: image.png
         :width: 90%
         :align: center

         Image title

     And a video below it all (yes, this is a hack):

     .. raw:: html

        <video width="832" height="390" preload="auto" autoplay controls loop>
           <source src="video.webm" type="video/webm">
        </video>

* Don't put a lot of text on one slide.  "3 to 7 things" is a good rule (though there are
  cases where more/less makes sense). The slide above is too big.

* If you want to build the slides, look at **Hieroglyph**:
  https://github.com/nyergler/hieroglyph 

  (otherwise, the maintainer will fix overfull/misaligned slides for you)


Contributors

-------
License
-------


All logos, videos and images found in the `topics/` subdirectory of this repository are
the property of their respective owners unless otherwise noted.

.. image:: https://i.creativecommons.org/l/by/3.0/88x31.png

All text content is licensed under a `Creative Commons Attribution 3.0 Unported License
<http://creativecommons.org/licenses/by/3.0/>`_
