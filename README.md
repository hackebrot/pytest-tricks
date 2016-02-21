# pytest-tricks
Tips and Tricks for the Python Testing Tool

http://hackebrot.github.io/pytest-tricks/

Getting Started
---------------

Install [lektor] and [npm].

Now we need to install the dependecies for this site:

```no-highlight
$ cd webpack
$ npm install
```

Launch Development Server
------------------------

Using the lektor CLI we launch a server at ``http://127.0.0.1:5000``:

```no-highlight
$ lektor server -f webpack
```

Changing the contents of the site automatically triggers a rebuild.


Deployment
----------

Commits to ``master`` get deployed automatically by [travis-ci].


Code of Conduct
---------------

Everyone interacting in the pytest-tricks project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the [PyPA Code of Conduct].

  [PyPA Code of Conduct]: https://www.pypa.io/en/latest/code-of-conduct/
  [lektor]: https://www.getlektor.com/downloads/
  [npm]: https://docs.npmjs.com/getting-started/installing-node
  [travis-ci]: https://travis-ci.org/hackebrot/pytest-tricks
