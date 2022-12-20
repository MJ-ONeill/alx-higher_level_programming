
#include <python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <stdlib.h>
#include <float.h>

void print_python_float(PyObject *p)
{
	PyFloatObject *f = (PyFloatObject *)p;
	double d = f->ob_fval;
	char *str = NULL;

	printf("[.] float object info\n");
	if (!PyFloat_Check(f))
        {
		printf("  [ERROR] Invalid Float Object\n");
		return		
	}
			        
	str = PyOS_double_to_string(d, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}

void print_python_bytes(PyObject *p)
{
	long unsigned int size;
	unsigned int i;
	char *trying_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		
