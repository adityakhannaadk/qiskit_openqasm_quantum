OPENQASM 2.0;
include "qelib1.inc";

qreg q[5];
creg c[5];

h q[0];
u1(pi/2) q[0];
cx q[0],q[1];
u1(pi/2) q[1];
cx q[0],q[1];
u1(pi/2) q[0];
u1(pi/2) q[1];
h q[1];
cx q[0],q[2];
u1(pi/2) q[2];
cx q[0],q[2];
u1(pi/2) q[1];
u1(pi/2) q[2];
cx q[1],q[2];
u1(pi/2) q[2];
cx q[1],q[2];
u1(pi/2) q[2];
h q[2];
measure q -> c;
