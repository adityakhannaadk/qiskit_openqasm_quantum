OPENQASM 2.0;
include "qelib1.inc";

qreg q[5];
creg c[5];

h q[3];
x q[4];
rx(pi/2) q[2];
cx q[2],q[3];
h q[4];
h q[2];
rz(pi/2) q[3];
ccx q[0],q[1],q[2];
cx q[3],q[4];
sdg q[1];
cswap q[2],q[3],q[4];
rx(pi/2) q[1];
reset q[3];
measure q[4] -> c[4];
cx q[1],q[2];
measure q[3] -> c[3];
s q[1];
measure q[2] -> c[2];
measure q[1] -> c[1];
measure q[0] -> c[0];
