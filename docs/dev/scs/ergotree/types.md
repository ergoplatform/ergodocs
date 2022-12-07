$$
\newcommand{\TEnv}{\Gamma}
\newcommand{\Der}[2]{#1~\vdash~#2}
\newcommand{\DerV}[2]{#1~\vdash^{\text{\lst{v}}}~#2}
\newcommand{\DerC}[2]{#1~\vdash^{\text{\lst{c}}}~#2}
\newcommand{\DerEnv}[1]{\Der{\TEnv}{#1}}
\newcommand{\DerEnvV}[1]{\DerV{\TEnv}{#1}}
\newcommand{\DerEnvC}[1]{\DerC{\TEnv}{#1}}
\newcommand{\lst}[1]{#1}
\newcommand{\Tup}[1]{(#1)}
\newcommand{\Apply}[2]{#1\langle#2\rangle}
\newcommand{\MSig}[3]{\text{def}~#1(#2): #3}
\newcommand{\Ov}[1]{\overline{#1}}
\newcommand{\TyLam}[3]{\lambda(\Ov{#1:#2}).#3}
\newcommand{\Trait}[2]{\text{trait}~#1~\{ #2 \}}
\newcommand{\To}{\mapsto}
\newcommand{\Low}[1]{\mathcal{L}{[\![#1]\!]}}
\newcommand{\Lam}[2]{\lambda#1.#2}
\newcommand{\IfThenElse}[3]{\text{if}~(#1)~#2~\text{else}~#3}
\newcommand{\False}{\text{false}}
\newcommand{\True}{\text{true}}
\newcommand{\langname}{ErgoTree}
\newcommand{\corelang}{$Core-}\lambda
$$

# Type Serialization

> This page is a WIP. Please see [ErgoTree.pdf](https://storage.googleapis.com/ergo-cms-media/docs/ErgoTree.pdf) for full details.
> 

In this section, we describe how the types (like \lst{Int}, \lst{Coll[Byte]},
etc.) are serialized; then, we define the serialization of typed data. This will
give us a basis to describe the serialization of Constant nodes of \ASDag. From
that, we proceed to serialization of arbitrary \ASDag trees.

For the motivation behind this type of encoding, please see Appendix~\ref{sec:appendix:motivation:type}.

## Distribution of type codes


The whole space of 256 codes is divided as the following:


$$\bf{Interval}$$ \& \bf{Distribution}

$$\lst{0x00}$$ \& special value to represent undefined type (\lst{NoType} in \ASDag)

$$\lst{0x01 - 0x6F(111)}$$ & data types including primitive types, arrays, options
aka nullable types, classes (in future), 111 = 255 - 144 different codes 

\lst{0x70(112) - 0xFF(255)} & function types \lst{T1 => T2}, 144 = 12 x 12
different codes 
 

### Encoding Data Types

There are nine different values for primitive types, and two more are reserved for future extensions.
Each primitive type has an id in a range {1,...,11} as the following.


1     &   Boolean   
2     &   Byte  
3     &   Short (16 bit)  
4     &   Int (32 bit)  
5     &   Long (64 bit)  
6     &   BigInt (java.math.BigInteger)  
7     &   GroupElement (org.bouncycastle.math.ec.ECPoint)  
8     &   SigmaProp   
9     &   reserved for Char   
10    &   reserved for Double   
11    &   reserved   


For each type constructor like $\lst{Coll}$ or $\lst{Option}$ we use the encoding
schema defined below. Type constructor has associated $\emph{base code}$ (e.g.
12 for $\lst{Coll[_]}$, 24 for $\lst{Coll[Coll[_]]}$ etc. ), which is multiple of
12.
Base code can be added to primitive type id to produce code of constructed
type; for example, 12 + 1 = 13 is a code of \lst{Coll[Byte]}. The code of the type constructor (12 in this example) is used when the type parameter is a non-primitive type (e.g. \lst{Coll[(Byte, Int)]}). In this case, the code of type
constructor is read first, and then recursive descent is performed to read
bytes of the parameter type (in this case \lst{(Byte, Int)}) This encoding
allows very simple and quick decoding by using div and mod operations.

The interval of codes for data types is divided as the following:

\begin{figure}[h] \footnotesize
    \(\begin{tabularx}{\textwidth}{| l | l | X |}

\bf{Interval} & \bf{Type constructor} & \bf{Description}  
0x01 - 0x0B(11)     &                    & primitive types (including 2 reserved)  
0x0C(12)            & \lst{Coll[_]}          & Collection of non-primitive types (\lst{Coll[(Int,Boolean)]})  
0x0D(13) - 0x17(23) & \lst{Coll[_]}          & Collection of primitive types (\lst{Coll[Byte]}, \lst{Coll[Int]}, etc.)  
0x18(24)            & \lst{Coll[Coll[_]]}    & Nested collection of non-primitive types (\lst{Coll[Coll[(Int,Boolean)]]})  
0x19(25) - 0x23(35) & \lst{Coll[Coll[_]]}    & Nested collection of primitive types (\lst{Coll[Coll[Byte]]}, \lst{Coll[Coll[Int]]})  
0x24(36)            & \lst{Option[_]}        & Option of non-primitive type (\lst{Option[(Int, Byte)]})  
0x25(37) - 0x2F(47) & \lst{Option[_]}        & Option of primitive type (\lst{Option[Int]})  
0x30(48)            & \lst{Option[Coll[_]]}  & Option of Coll of non-primitive type (\lst{Option[Coll[(Int, Boolean)]]})  
0x31(49) - 0x3B(59) & \lst{Option[Coll[_]]}  & Option of Coll of primitive type (\lst{Option[Coll[Int]]})  
0x3C(60)            & \lst{(_,_)}            & Pair of non-primitive types (\lst{((Int, Byte), (Boolean,Box))}, etc.)  
0x3D(61) - 0x47(71) & \lst{(_, Int)}         & Pair of types where first is primitive (\lst{(_, Int)})  
0x48(72)            & \lst{(_,_,_)}          & Triple of types   
0x49(73) - 0x53(83) & \lst{(Int, _)}         & Pair of types where second is primitive (\lst{(Int, _)})  
0x54(84)            & \lst{(_,_,_,_)}        & Quadruple of types   
0x55(85) - 0x5F(95) & \lst{(_, _)}           & Symmetric pair of primitive types (\lst{(Int, Int)}, \lst{(Byte,Byte)}, etc.)  
0x60(96)            & \lst{(_,...,_)}        & \lst{Tuple} type with more than 4 items \lst{(Int, Byte, Box, Boolean, Int)}  
0x61(97)            & \lst{Any}             & Any type   
0x62(98)            & \lst{Unit}            & Unit type  
0x63(99)            & \lst{Box}             & Box type   
0x64(100)           & \lst{AvlTree}         & AvlTree type   
0x65(101)           & \lst{Context}         & Context type   
0x65(102)           & \lst{String}          & String   
0x66(103)           & \lst{IV}              & TypeIdent   
0x67(104)- 0x6E(110)&                    & reserved for future use   
0x6F(111)           &                    & Reserved for future \lst{Class} type (e.g. user-defined types)   
\end{tabularx}\)
\label{fig:ser:type:primtypes}
\end{figure}

\subsubsection{Encoding Function Types}

We use $12$ different values for both domain and range types of functions. This
gives us $12 * 12 = 144$ function types in total and allows us to represent $11 *
11 = 121$ functions over primitive types using just a single byte.

Each code $F$ in a range of function types can be represented as
$F = D * 12 + R + 112$, where $D, R \in \{0,\dots,11\}$ - indices of domain and range types correspondingly, 
$112$ - is the first code in an interval of function types. 

If $D = 0$, then the domain type is not primitive and recursive descent is necessary to write/read the domain type.

If $R = 0$, then the range type is not primitive and recursive descent is necessary to write/read the range type.

\subsubsection{Recursive Descent}

When an argument of a type constructor is not a primitive type, we fallback to
the simple encoding schema.

In such a case, we emit the special code for the type constructor according to
the table above and descend recursively to every child node of the type tree.

We do this descend only for those children whose code cannot be embedded in
the parent code. For example, serialization of \lst{Coll[(Int,Boolean)]}
proceeds as the following:
\begin{enumerate}
\item emit \lst{0x0C} because element of collection is not primitive 
\item recursively serialize \lst{(Int, Boolean)}
\item emit \lst{0x3D} because the first item in the pair is primitive
\item recursively serialize \lst{Boolean}
\item emit \lst{0x02} - the code for primitive type \lst{Boolean}
\end{enumerate}

\noindent Examples

\begin{figure}[h] \footnotesize
\(\begin{tabularx}{\textwidth}{| l | c | c | l | c | X |}

\bf{Type}                &\bf{D} & \bf{R} & \bf{Bytes} & \bf{\#Bytes} &  \bf{Comments}  
\lst{Byte}               &     &     &  1                   &  1     &     
\lst{Coll[Byte]}         &     &     &  12 + 1 = 13         &  1     &     
\lst{Coll[Coll[Byte]]}   &     &     &  24 + 1 = 25         &  1     &      
\lst{Option[Byte]}       &     &     &  36 + 1 = 37         &  1     & register     
\lst{Option[Coll[Byte]]} &     &     &  48 + 1 = 49         &  1     & register     
\lst{(Int,Int)}          &     &     &  84 + 3 = 87         &  1     & fold     
\lst{Box=>Boolean}       & 7   & 2   &  198 = 7*12+2+112    &  1     & exist, for all     
\lst{(Int,Int)=>Int}     & 0   & 3   &  115=0*12+3+112, 87  &  2     &  fold     
\lst{(Int,Boolean)}      &     &     &  60 + 3, 2           &  2     &       
\lst{(Int,Box)=>Boolean} & 0   & 2   &  0*12+2+112, 60+3, 7 &  3     &      
\end{tabularx}\)
\label{fig:ser:type:primtypes}
\end{figure}
