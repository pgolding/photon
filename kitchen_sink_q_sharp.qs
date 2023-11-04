namespace Quantum.QB4 {

    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Diagnostics;
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Math;

    function DoubleAsString(value : Double) : String {
        return $"{value}";
    }

    @EntryPoint()
    operation QB4Run() : Unit {
        Message("Hello quantum weirdness!");

        // Set up counters for our definite qubit states
        mutable num0000 = 0;
		mutable num0001 = 0;
		mutable num0010 = 0;
		mutable num0011 = 0;
		mutable num0100 = 0;
		mutable num0101 = 0;
		mutable num0110 = 0;
		mutable num0111 = 0;
		mutable num1000 = 0;
		mutable num1001 = 0;
		mutable num1010 = 0;
		mutable num1011 = 0;
		mutable num1100 = 0;
		mutable num1101 = 0;
		mutable num1110 = 0;
		mutable num1111 = 0;

        // Allocate four qubits.
        use qubits = Qubit[4];

        mutable index = 0;
        let iterations = 10000;
        while index < iterations {

            // do nothing -- i.e. just initialize qubits
            Set (Zero, qubits[0]);
		    //Set (Zero, qubits[1]);
		    //Set (Zero, qubits[2]);
		    Set (Zero, qubits[3]);

            //Demo of pass through (NOP)
			Set (One, qubits[1]);
			Set (One, qubits[2]);

            //Demo of NOT gate
		    //Set (Zero, qubits[0]);
			X(qubits[0]);

            //Demo of Hadamard
			H(qubits[0]);

            //Demo of SWAP
			SWAP (qubits[0],qubits[1]);

            //Demo of Controlled-NOT   ( CNOT )
			CNOT(qubits[0],qubits[1]);

            //Demo of Bell State
			H(qubits[0]);
		    CNOT(qubits[0],qubits[1]);

            //Demo of Toffoli Gate in general configuration
            CCNOT(qubits[0],qubits[1],qubits[2]);

            //Demo of Toffoli Gate in NOT configuration
            Set (One, qubits[0]); // Always 1
            Set (One, qubits[1]); // Always 1
            Set (One, qubits[2]); // Input of NOT gate. Gets inverted by NOT
            CCNOT(qubits[0],qubits[1],qubits[2]);

            //Demo of Toffoli Gate in AND configuration
            Set (One, qubits[0]); // Input 1 of AND
            Set (One, qubits[1]); // Input 2 of AND
            Set (Zero, qubits[2]);// Initialized to 0. Gets the result of AND
            CCNOT(qubits[0],qubits[1],qubits[2]);

            //Demo of Toffoli Gate in FANOUT configuration
            Set (One, qubits[0]); // Always 1
            Set (One, qubits[1]); // Input & Pass through.
            Set (Zero, qubits[2]); //Initialized to 0. Gets a result of the fanout from qubits[1]
            CCNOT(qubits[0],qubits[1],qubits[2]);

            // measure the qubits
            let res0 = M (qubits[0]);
            let res1 = M (qubits[1]);
            let res2 = M (qubits[2]);
            let res3 = M (qubits[3]);

            if(res3 == Zero and res2 == Zero and res1 == Zero and res0 == Zero){set num0000 = num0000 + 1;}
            if(res3 == Zero and res2 == Zero and res1 == Zero and res0 == One ){set num0001 = num0001 + 1;}
            if(res3 == Zero and res2 == Zero and res1 == One  and res0 == Zero){set num0010 = num0010 + 1;}
            if(res3 == Zero and res2 == Zero and res1 == One  and res0 == One ){set num0011 = num0011 + 1;}
            if(res3 == Zero and res2 == One  and res1 == Zero and res0 == Zero){set num0100 = num0100 + 1;}
            if(res3 == Zero and res2 == One  and res1 == Zero and res0 == One ){set num0101 = num0101 + 1;}
            if(res3 == Zero and res2 == One  and res1 == One  and res0 == Zero){set num0110 = num0110 + 1;}
            if(res3 == Zero and res2 == One  and res1 == One  and res0 == One ){set num0111 = num0111 + 1;}
            if(res3 == One  and res2 == Zero and res1 == Zero and res0 == Zero){set num1000 = num1000 + 1;}
            if(res3 == One  and res2 == Zero and res1 == Zero and res0 == One ){set num1001 = num1001 + 1;}
            if(res3 == One  and res2 == Zero and res1 == One  and res0 == Zero){set num1010 = num1010 + 1;}
            if(res3 == One  and res2 == Zero and res1 == One  and res0 == One ){set num1011 = num1011 + 1;}
            if(res3 == One  and res2 == One  and res1 == Zero and res0 == Zero){set num1100 = num1100 + 1;}
            if(res3 == One  and res2 == One  and res1 == Zero and res0 == One ){set num1101 = num1101 + 1;}
            if(res3 == One  and res2 == One  and res1 == One  and res0 == Zero){set num1110 = num1110 + 1;}
            if(res3 == One  and res2 == One  and res1 == One  and res0 == One ){set num1111 = num1111 + 1;}
            
            set index += 1;
        } 

        // inspect the quantum machine
        DumpMachine();

        let loops = IntAsDouble(iterations);        
        Message("0000 -> " + DoubleAsString(IntAsDouble(num0000)/loops));
        Message("0001 -> " + DoubleAsString(IntAsDouble(num0001)/loops));
        Message("0010 -> " + DoubleAsString(IntAsDouble(num0010)/loops));
        Message("0011 -> " + DoubleAsString(IntAsDouble(num0011)/loops));
        Message("0100 -> " + DoubleAsString(IntAsDouble(num0100)/loops));
        Message("0101 -> " + DoubleAsString(IntAsDouble(num0101)/loops));
        Message("0110 -> " + DoubleAsString(IntAsDouble(num0110)/loops));
        Message("0111 -> " + DoubleAsString(IntAsDouble(num0111)/loops));
        Message("1000 -> " + DoubleAsString(IntAsDouble(num1000)/loops));
        Message("1001 -> " + DoubleAsString(IntAsDouble(num1001)/loops));
        Message("1010 -> " + DoubleAsString(IntAsDouble(num1010)/loops));
        Message("1011 -> " + DoubleAsString(IntAsDouble(num1011)/loops));
        Message("1100 -> " + DoubleAsString(IntAsDouble(num1100)/loops));
        Message("1101 -> " + DoubleAsString(IntAsDouble(num1101)/loops));
        Message("1110 -> " + DoubleAsString(IntAsDouble(num1110)/loops));
        Message("1111 -> " + DoubleAsString(IntAsDouble(num1111)/loops));

        // Release qubits to ket0 state, as required by Q# simulator
        Set(Zero, qubits[0]);
		Set(Zero, qubits[1]);
		Set(Zero, qubits[2]);
		Set(Zero, qubits[3]);
    }

    operation Set (desired: Result, q1: Qubit) : Unit
    {
		let current = M(q1);
		if (desired != current)
		{
			X(q1);
		}   
    }
}