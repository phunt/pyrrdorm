# PyRRDORM
Expands on python-rrdtool -- make it simple to capture rrdtool based
data and manage tables (files).

Currently in "works for me" state. ;-)

- pyrrdorm.py contains base level functionality
- pyrrdorm_stdtables.py contains basic data table definitions
- proc_impl.py implemtations of stdtables based on proc filesystem

- capture.py is user specific and specifies what data to capture,
how to capture it (impl) and where to put the output

- graph.py is currently hardcoded to output some basic graphs, needs
to be worked on to automatically generate the graphs based on the
table definitions.

Feel free to try it out.
