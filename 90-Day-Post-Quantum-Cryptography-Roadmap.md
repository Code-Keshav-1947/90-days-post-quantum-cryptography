# 90-Day Post-Quantum Cryptography Foundation Challenge

> **Goal:** Build a serious foundation in mathematics, cryptography, cybersecurity, quantum computing, and modern post-quantum cryptography—then finish with a working capstone.
>
> **Starting assumption:** You are a programmer who already knows Python and web development, but you are not expected to know university-level cryptography or quantum computing.
>
> **Time target:** 60–120 minutes/day. If you have less time, keep the order and reduce the depth rather than skipping foundations.

---

## What You Should Be Able to Do After 90 Days

By Day 90, you should be able to:

- Explain why RSA and ECC are threatened by quantum computing.
- Use modular arithmetic, finite fields, vectors, matrices, probability, and basic abstract algebra.
- Explain public-key encryption, KEMs, signatures, hashes, authentication, and key exchange.
- Explain Shor's and Grover's algorithms at a conceptual level.
- Understand the basic intuition behind lattices, LWE, Module-LWE, SIS, and hash-based signatures.
- Read the high-level structure of ML-KEM and ML-DSA standards.
- Understand why a toy implementation is educational but should not be used as production cryptography.
- Build and document a small PQC demonstration.
- Continue into research papers, standards, implementation, and cryptanalysis with a much stronger foundation.

## Important Current Standardization Context

As of September 2026, NIST's first three finalized PQC standards are:

- **FIPS 203 — ML-KEM**, a module-lattice-based key-encapsulation mechanism.
- **FIPS 204 — ML-DSA**, a module-lattice-based digital signature standard.
- **FIPS 205 — SLH-DSA**, a stateless hash-based digital signature standard.

NIST selected **HQC** for standardization in March 2025 as an additional KEM, and work on additional signature algorithms continues. Always check the current NIST material before treating this roadmap's algorithm list as permanently final.

Sources:

- NIST PQC project: https://csrc.nist.gov/Projects/Post-Quantum-Cryptography
- FIPS 203/204/205 information: https://csrc.nist.gov/Projects/Post-Quantum-Cryptography/Post_Quantum_Cryptography-Standardization
- NIST PQC publications: https://csrc.nist.gov/Projects/post-quantum-cryptography/publications

---

# How to Use This Challenge

Every day has four parts:

1. **Learn** — theory/math.
2. **Implement** — write code yourself.
3. **Explain** — write a short explanation in your own words.
4. **Checkpoint** — answer questions without looking at notes.

### Rules

- Do not copy cryptography code blindly.
- Never invent your own production cryptographic algorithm.
- For toy implementations, deliberately use tiny parameters so the mathematics is visible.
- For real applications, use vetted libraries and standardized algorithms.
- Keep a Git repository with folders:
  - `notes/`
  - `math/`
  - `crypto/`
  - `quantum/`
  - `pqc/`
  - `projects/`
  - `research-notes/`
- Commit every day.
- Keep a `LEARNING_LOG.md`.
- Whenever you learn an algorithm, answer: **What problem does it solve? What assumption makes it hard? What information is public? What must remain secret?**

---

# PHASE 1 — Mathematical Foundations

## Days 1–20

The objective is not to become a mathematician. It is to acquire the mathematical language used by cryptography.

---

## Day 1 — Cryptography Map

`Done`
`Date: 25|09|2026`

Learn:

- Symmetric vs asymmetric cryptography
- Encryption vs authentication vs signatures
- Classical cryptography vs PQC
- Why quantum computers matter

Build:

- Create the repository.
- Write a one-page `what-is-pqc.md`.

Checkpoint:

- What exactly is "post-quantum"?
- Why is PQC not the same thing as quantum cryptography?

---

## Day 2 — Integers, Divisibility and Primes

Learn:

- Divisibility
- Prime numbers
- Composite numbers
- Factorization
- Fundamental theorem of arithmetic

Implement:

- Prime checker
- Prime generator
- Trial-division factorization

Project:
**Prime Detective** — make a small CLI that analyzes an integer and reports its factors and primality.

---

## Day 3 — GCD

Learn:

- Greatest common divisor
- Euclidean algorithm

Implement:

- `gcd(a, b)`

Challenge:

- Count how many Euclidean steps are required for different inputs.

---

## Day 4 — Extended Euclidean Algorithm

Learn:

- Bézout identity
- Extended GCD

Implement:

- `extended_gcd(a, b)`

Understand:
`ax + by = gcd(a,b)`

---

## Day 5 — Modular Arithmetic

Learn:

- Congruence
- Addition/multiplication modulo n
- Modular equivalence

Implement:

- Modular calculator

Checkpoint:
Explain why:

`17 ≡ 5 (mod 12)`

---

## Day 6 — Modular Inverses

Learn:

- What an inverse modulo n means
- When an inverse exists

Implement:

- `mod_inverse(a, n)` using extended GCD

Project upgrade:
Build a modular-arithmetic CLI.

---

## Day 7 — Weekly Challenge #1

Without tutorials:

1. Implement GCD.
2. Implement Extended GCD.
3. Implement modular inverse.
4. Solve several modular equations.
5. Explain each result.

**Milestone:** You should be comfortable with modular arithmetic.

---

## Day 8 — Exponentiation

Learn:

- Modular exponentiation
- Repeated squaring

Implement:

- Fast modular exponentiation

Challenge:
Compare naive exponentiation with repeated squaring.

---

## Day 9 — Fermat's Little Theorem

Learn:

- Fermat's Little Theorem
- Why primes appear everywhere in cryptography

Implement:

- A modular exponentiation experiment that verifies the theorem for many small primes.

---

## Day 10 — Euler's Totient Function

Learn:

- `φ(n)`
- Coprime numbers
- Euler's theorem

Implement:

- `phi(n)`

Mini-project:
**Number Theory Explorer**

Features:

- prime test
- gcd
- phi
- modular inverse
- modular exponentiation

---

## Day 11 — Chinese Remainder Theorem

Learn:

- CRT
- Why a problem can be split into smaller modular problems

Implement:

- CRT for pairwise-coprime moduli.

---

## Day 12 — Probability Fundamentals

Learn:

- Sample space
- Events
- Conditional probability
- Independence

Implement:

- Coin/dice simulation.

Connect it to:

- Randomness in cryptography.

---

## Day 13 — Random Variables

Learn:

- Random variables
- Expected value
- Variance
- Probability distributions

Project:
Simulate a random process 100,000 times and compare empirical results with theory.

---

## Day 14 — Information and Entropy

Learn:

- Information intuition
- Entropy
- Min-entropy
- Why predictable randomness is dangerous

Do not confuse:

- Random-looking output
- Cryptographically secure randomness

---

## Day 15 — Vectors

Learn:

- Vectors
- Addition
- Scalar multiplication
- Dot product
- Norms

Implement:

- Vector operations from scratch.

---

## Day 16 — Matrices

Learn:

- Matrix representation
- Matrix multiplication
- Identity matrix
- Inverses

Implement:

- Matrix multiplication.

---

## Day 17 — Linear Algebra

Learn:

- Linear independence
- Basis
- Span
- Rank

Connect:

- Why linear algebra appears in lattice cryptography.

---

## Day 18 — Polynomials

Learn:

- Polynomial arithmetic
- Degree
- Polynomial multiplication
- Remainders

Implement:

- Polynomial addition/multiplication.

---

## Day 19 — Finite Fields Preview

Learn:

- What a field is
- Why finite fields matter
- `GF(p)` intuition

Do not rush abstract algebra. Understand examples first.

---

## Day 20 — Mathematics Gate

You pass this phase when you can explain and implement:

- GCD
- Extended GCD
- Modular inverse
- Modular exponentiation
- CRT
- Basic probability
- Vectors
- Matrices
- Polynomial arithmetic

**Project 1 complete: Number Theory Explorer**

---

# PHASE 2 — Classical Cryptography

## Days 21–40

Now you learn the cryptographic world that PQC is trying to protect or replace.

---

## Day 21 — Cryptographic Goals

Learn:

- Confidentiality
- Integrity
- Authentication
- Non-repudiation
- Threat models

Write:
`security-goals.md`

---

## Day 22 — Hash Functions

Learn:

- One-wayness
- Collision resistance
- Preimage resistance
- Avalanche effect

Use:

- SHA-256 from a standard library.

Important:
Do not implement SHA-256 as a production replacement.

---

## Day 23 — Hash Experiment

Project:
**Hash Avalanche Lab**

Change one bit of an input and measure how much the output changes.

---

## Day 24 — Symmetric Cryptography

Learn:

- Block ciphers
- Stream ciphers
- Keys
- IVs/nonces
- Modes of operation
- AEAD

Study:

- AES-GCM conceptually.

---

## Day 25 — Secure Password Storage

Learn:

- Password hashing
- Salt
- Slow password KDFs
- Why plain SHA-256 is not a password-storage solution

Project:
Build a toy password-storage demo using a proper password hashing library.

---

## Day 26 — Public-Key Cryptography

Learn:

- Public/private keys
- Trapdoor functions
- Key establishment
- Digital signatures

---

## Day 27 — RSA Mathematics

Learn:

- Key generation
- Euler's theorem
- Encryption/decryption intuition
- Why factoring matters

Project:
**Toy RSA**

Use tiny educational parameters only.

---

## Day 28 — Break Your Toy RSA

Try:

- Small primes
- Small keys
- Naive factorization

Goal:
Understand that RSA security depends on parameter sizes and computational assumptions.

---

## Day 29 — Diffie-Hellman

Learn:

- Key exchange
- Discrete logarithm problem
- Man-in-the-middle attack

Project:
Implement toy Diffie-Hellman.

---

## Day 30 — Elliptic-Curve Cryptography

Learn conceptually:

- Elliptic-curve points
- Point addition
- Scalar multiplication
- Discrete logarithm assumption

You do not need advanced elliptic-curve mathematics yet.

---

## Day 31 — Digital Signatures

Learn:

- Signing
- Verification
- Integrity
- Authentication

Study:

- RSA signatures
- ECDSA conceptually

---

## Day 32 — Certificates and PKI

Learn:

- Certificates
- Certificate authorities
- Trust chains
- Public-key infrastructure

---

## Day 33 — TLS

Learn:

- What happens during HTTPS
- Handshake
- Key establishment
- Symmetric session encryption
- Authentication

Project:
Draw your own simplified TLS handshake diagram.

---

## Day 34 — Cryptographic Attacks

Learn:

- Brute force
- Dictionary attacks
- MITM
- Replay
- Padding/oracle intuition
- Weak randomness
- Key reuse

---

## Day 35 — Computational Hardness

Learn:

- Efficient vs infeasible
- Polynomial vs exponential
- Security parameters
- Reduction intuition

Critical question:

> "Hard for whom, with what resources, and under which model?"

---

## Day 36 — Complexity

Learn:

- Big-O
- Polynomial time
- Exponential time
- Sub-exponential intuition

Connect:

- Cryptographic security assumptions.

---

## Day 37 — Classical Crypto Lab

Build:

**Mini Secure Messenger — Classical Edition**

Features:

- Key establishment
- Symmetric encryption
- Authentication/integrity
- Message exchange

Keep it educational, not production security.

---

## Day 38 — Why Quantum Changes the Model

Study:

- Classical computer assumptions
- Quantum computer capabilities
- Shor
- Grover

---

## Day 39 — Shor's Algorithm

Understand conceptually:

`Quantum period finding → factoring/discrete logarithms → RSA/ECC threat`

Do not try to implement the full algorithm mathematically yet.

---

## Day 40 — Classical Crypto Gate

You should be able to explain:

- Hash
- MAC
- Encryption
- KEM/key exchange
- Digital signature
- RSA
- Diffie-Hellman
- ECC
- TLS
- Why RSA/ECC are threatened by quantum computing

**Project 2 complete: Classical Secure Messenger**

---

# PHASE 3 — Quantum Computing Foundations

## Days 41–55

You are learning enough quantum computing to understand the threat—not trying to become a quantum physicist.

---

## Day 41 — Quantum vs Classical Information

Learn:

- Bit
- Qubit
- State vector intuition

---

## Day 42 — Complex Numbers

Learn:

- Complex numbers
- Magnitude
- Phase
- Complex vector intuition

This connects directly to quantum state mathematics.

---

## Day 43 — Qubit Mathematics

Learn:

- Dirac notation intuition
- Basis states
- Superposition
- Normalization

---

## Day 44 — Measurement

Learn:

- Measurement
- Probabilities
- Collapse as an operational model

Build:

- Tiny qubit measurement simulator.

---

## Day 45 — Quantum Gates

Learn:

- X
- Z
- H
- Basic gate composition

Project:
**Quantum Gate Playground**

Represent small state vectors and apply simple gates.

---

## Day 46 — Multiple Qubits

Learn:

- Tensor-product intuition
- Two-qubit states
- Entanglement

---

## Day 47 — Quantum Circuits

Build:

- Small circuit simulator for selected gates.

---

## Day 48 — Grover's Algorithm

Learn:

- Search problem
- Classical search
- Quantum speedup intuition

Understand:
Grover gives roughly a quadratic speedup for generic unstructured search, which affects security margins for symmetric cryptography.

---

## Day 49 — Shor's Algorithm Deep Dive

Study:

- Factoring
- Period finding
- Why the quantum part matters

Draw the pipeline.

---

## Day 50 — Quantum Threat Model

Create a table:

| Classical primitive | Quantum concern                              |
| ------------------- | -------------------------------------------- |
| RSA                 | Shor                                         |
| Diffie-Hellman      | Shor                                         |
| ECC                 | Shor                                         |
| AES                 | Grover-related search speedup                |
| SHA-2               | Grover-related generic search considerations |

Explain the table in your own words.

---

## Day 51 — Quantum Security Thinking

Learn:

- Security levels
- Attack cost
- Asymptotic vs concrete security
- Quantum vs classical attackers

---

## Day 52 — Quantum Mini Project

**Toy Grover Lab**

Compare classical brute-force search with a simplified Grover-style simulation.

---

## Day 53 — Quantum Computing Review

Without notes, explain:

- Qubit
- Superposition
- Measurement
- Entanglement
- Gate
- Circuit
- Grover
- Shor

---

## Day 54 — Bridge to PQC

Answer:

> If RSA/ECC are threatened, what kinds of mathematical problems could replace factoring/discrete logarithms?

Research:

- Lattice problems
- Codes
- Hashes
- Other assumptions

---

## Day 55 — Quantum Gate

**Project 3 complete: Quantum Threat Lab**

You should now understand _why_ PQC exists.

---

# PHASE 4 — Post-Quantum Cryptography

## Days 56–75

This is the core of the challenge.

---

## Day 56 — PQC Landscape

Learn the major families:

- Lattice-based
- Code-based
- Hash-based
- Multivariate
- Isogeny-based history
- Symmetric cryptography as a quantum-resistant foundation

---

## Day 57 — What Is a Lattice?

Learn:

- Lattice
- Basis
- Lattice vectors
- Dimension
- Fundamental region
- Norm

Implement:

- 2D lattice visualizer.

---

## Day 58 — Lattice Geometry

Study:

- Short vectors
- Long vectors
- Basis changes
- Geometric intuition

Project:
**Lattice Visualizer**

Input a 2D basis and plot lattice points.

---

## Day 59 — SVP and CVP

Learn:

- Shortest Vector Problem
- Closest Vector Problem

Understand why they matter.

Do not assume:
"Hard" automatically means "secure." Security requires careful assumptions and reductions.

---

## Day 60 — Learning With Errors

This is a major milestone.

Learn the intuition:

`b = A·s + e`

where:

- `A` is public
- `s` is secret
- `e` is small noise

Understand why the noise changes an easy linear system into a hard problem.

---

## Day 61 — Toy LWE

Implement:

**Toy LWE Encryption**

Use tiny matrices and deliberately small dimensions.

Goal:
Understand the role of noise.

---

## Day 62 — LWE Attack Experiment

Try to solve your toy LWE instances using brute force.

Observe how parameter size changes the problem.

---

## Day 63 — Polynomial Rings

Learn:

- Polynomial addition
- Multiplication
- Reduction modulo a polynomial
- Ring notation intuition

---

## Day 64 — Ring-LWE

Learn:

- Why polynomials can compress structure
- Ring-LWE intuition
- Why structured algebra is useful

---

## Day 65 — Module-LWE

Learn:

- Modules as a middle ground between vectors and rings
- Why Module-LWE is important to modern NIST-standardized lattice schemes

---

## Day 66 — SIS

Learn:

- Short Integer Solution
- Relationship to lattice problems
- Why SIS appears in signatures

---

## Day 67 — KEMs

Learn:

- Key Encapsulation Mechanism
- Key generation
- Encapsulation
- Decapsulation

Understand the distinction:

`KEM ≠ ordinary encryption`

---

## Day 68 — ML-KEM Architecture

Study FIPS 203 at a high level.

Trace:

- Key generation
- Encapsulation
- Decapsulation
- Polynomial arithmetic
- Noise
- Compression/encoding

Do not attempt to memorize the standard.

---

## Day 69 — ML-KEM Parameter Exploration

Compare the standardized parameter sets and investigate:

- Key sizes
- Ciphertext sizes
- Shared-secret behavior
- Performance

Use official standards/current documentation.

---

## Day 70 — ML-KEM Implementation Study

Use a vetted implementation/library.

Your job:

- Generate keys
- Encapsulate
- Decapsulate
- Verify shared secrets match

**Do not invent a new implementation for real security use.**

---

## Day 71 — Lattice Signature Intuition

Learn:

- Why signatures need a different construction
- SIS
- Fiat-Shamir intuition
- Rejection sampling intuition

---

## Day 72 — ML-DSA Architecture

Study FIPS 204 at a high level.

Trace:

- Key generation
- Signing
- Verification
- Polynomial/vector operations
- Hashing
- Sampling

---

## Day 73 — Hash-Based Signatures

Learn:

- Merkle trees
- One-time signatures
- Hash-based signature construction
- Stateless vs stateful intuition

---

## Day 74 — SLH-DSA

Study FIPS 205.

Understand why a hash-based signature standard is valuable as a different mathematical approach from lattice signatures.

---

## Day 75 — PQC Families Gate

Create a comparison matrix:

| Family  | Main idea                     | Example             | Main trade-offs                          |
| ------- | ----------------------------- | ------------------- | ---------------------------------------- |
| Lattice | Hard lattice-related problems | ML-KEM, ML-DSA      | Size/complexity                          |
| Hash    | Security from hashes          | SLH-DSA             | Signature size/performance               |
| Code    | Hard decoding problems        | HQC                 | Different implementation/size trade-offs |
| Other   | Alternative assumptions       | Research candidates | Varies                                   |

Do not rank them globally. Compare them by measurable properties and use cases.

---

# PHASE 5 — Standards, Engineering & Security

## Days 76–85

Now move from "I understand the math" to "I understand how PQC is deployed."

---

## Day 76 — Read a Standard

Start reading selected portions of FIPS 203.

Do not read it cover-to-cover.

Learn to locate:

- Definitions
- Algorithms
- Parameters
- Encoding
- Security categories
- Implementation requirements

---

## Day 77 — Read FIPS 204

Focus on:

- ML-DSA algorithm flow
- Inputs/outputs
- Key/signature sizes
- Parameter sets

---

## Day 78 — Read FIPS 205

Focus on:

- Hash-based construction
- Signing
- Verification
- Parameter sets

---

## Day 79 — Crypto Agility

Learn:

- Why systems should not hard-code one cryptographic algorithm
- Algorithm identifiers
- Versioning
- Migration strategies
- Key rotation

Project:
Design a crypto-agile API interface.

---

## Day 80 — Hybrid Cryptography

Learn the idea of combining:

- Classical key establishment
- PQ key establishment

Understand why organizations may use hybrid approaches during migration.

---

## Day 81 — PQC Migration

Learn:

- Crypto inventory
- Vulnerable algorithm discovery
- Dependencies
- Certificates
- Protocol migration
- Long-lived data

---

## Day 82 — Harvest Now, Decrypt Later

Understand the threat model:

An attacker can collect encrypted traffic today and attempt decryption later if they eventually obtain the required quantum capability.

Do not treat this as proof that a large cryptographically relevant quantum computer exists today.

---

## Day 83 — Side-Channel Awareness

Learn:

- Timing attacks
- Cache attacks
- Power analysis
- Fault attacks
- Constant-time programming

Critical lesson:

**Mathematical security does not automatically imply implementation security.**

---

## Day 84 — Secure Implementation Engineering

Study:

- Secure randomness
- Memory safety
- Constant-time operations
- Input validation
- Error handling
- Key lifecycle
- Dependency management

---

## Day 85 — Engineering Gate

Audit your previous projects.

For each one, write:

- Threat model
- Secrets
- Attack surface
- Weaknesses
- What should never be used in production

---

# PHASE 6 — Capstone

## Days 86–90

This is where everything comes together.

# Project 4 — PQC Secure Messenger

Build an educational secure messaging prototype with a modular cryptographic interface.

Architecture:

```text
Client A
   |
   |  PQ KEM
   v
Shared Secret
   |
   v
KDF
   |
   v
AEAD Session Key
   |
   v
Encrypted Message
   |
   +---- PQ Signature ----> Authentication
```

The project should have replaceable crypto modules rather than hard-coded algorithms.

---

## Day 86 — Architecture

Design:

```text
crypto/
    interface.py
    classical.py
    pqc.py
    hashing.py
    kdf.py

protocol/
    handshake.py
    message.py

tests/
    test_crypto.py
    test_protocol.py

docs/
    threat-model.md
    architecture.md
```

---

## Day 87 — PQ KEM Integration

Using a vetted implementation/library:

- Generate PQ key pair
- Encapsulate
- Decapsulate
- Verify shared secret equality

Add tests.

---

## Day 88 — Authentication

Add a signature layer.

Test:

- Valid signature
- Modified message
- Wrong public key
- Invalid signature

---

## Day 89 — Final Security Review

Perform a mini threat model.

Ask:

1. What does the attacker see?
2. What is secret?
3. What happens if a message changes?
4. What happens if a public key changes?
5. What happens if a nonce is reused?
6. What happens if the RNG fails?
7. Which components are standardized?
8. Which parts are only educational?

Write:
`FINAL_SECURITY_REVIEW.md`

---

## Day 90 — PQC Researcher Day

Do not code.

Produce a final report:

# "What I Learned About Post-Quantum Cryptography"

Include:

1. Classical cryptography
2. Quantum threat
3. Shor's algorithm
4. Grover's algorithm
5. Lattices
6. LWE
7. Module-LWE
8. SIS
9. ML-KEM
10. ML-DSA
11. SLH-DSA
12. Migration
13. Implementation security
14. Open questions

Then give a 10-minute presentation to yourself or someone else.

If you can explain the entire system without reading your notes, you have completed the foundation.

---

# Major Projects

## Project 1 — Number Theory Explorer

**Days 2–20**

Python CLI containing:

- prime checking
- factorization
- GCD
- extended GCD
- modular inverse
- modular exponentiation
- Euler phi
- CRT

---

## Project 2 — Classical Secure Messenger

**Days 27–40**

Educational system demonstrating:

- public-key key establishment
- symmetric encryption
- authentication
- signatures
- attack demonstrations

---

## Project 3 — Quantum Threat Lab

**Days 41–55**

Build:

- qubit simulator
- gate simulator
- measurement experiment
- Grover-style search demonstration
- RSA/ECC quantum-threat visualization

---

## Project 4 — LWE Laboratory

**Days 60–66**

Build:

- LWE instance generator
- noise generator
- toy encryption
- brute-force solver
- parameter experiment

Graph:

- dimension vs attack effort
- noise vs decryption behavior

---

## Project 5 — Lattice Visualizer

**Days 57–60**

Interactive 2D visualization of:

- lattice basis
- lattice points
- shortest vectors
- closest vectors

---

## Project 6 — PQC Secure Messenger

**Days 86–90**

Final capstone using standardized PQC primitives through a vetted implementation.

---

# Your Daily Routine

Use this template every day:

```text
Date:
Day:

1. Concept I learned:
2. Math I learned:
3. Code I wrote:
4. Experiment:
5. What confused me:
6. Explanation in my own words:
7. Questions:
8. Git commit:
9. Confidence: /10
```

---

# Weekly Exams

At the end of every 7 days, close your notes.

Answer from memory.

### Week 1

Can you solve modular arithmetic problems?

### Week 2

Can you explain probability, vectors, matrices, and finite fields?

### Week 3

Can you explain hash functions and symmetric cryptography?

### Week 4

Can you explain RSA, DH, ECC, signatures, and TLS?

### Week 5

Can you explain why Shor threatens RSA/ECC?

### Week 6

Can you manipulate qubits and explain Grover/Shor conceptually?

### Week 7

Can you explain lattice problems?

### Week 8

Can you explain LWE, Ring-LWE, Module-LWE, and SIS?

### Week 9

Can you explain ML-KEM, ML-DSA, and SLH-DSA?

### Week 10

Can you explain PQC migration and crypto agility?

### Final

Can you teach PQC to another programmer?

---

# Mathematics You Should Eventually Master

## Tier 1 — Must Know

- Algebra
- Modular arithmetic
- GCD
- Extended Euclid
- Prime numbers
- Probability
- Vectors
- Matrices
- Polynomial arithmetic

## Tier 2 — Strongly Recommended

- Number theory
- Finite fields
- Abstract algebra
- Linear algebra
- Probability theory
- Complexity theory

## Tier 3 — PQC Deep Dive

- Lattices
- Norms
- SVP
- CVP
- LWE
- SIS
- Ring-LWE
- Module-LWE
- Polynomial rings
- Gaussian distributions
- Reduction concepts

## Tier 4 — Research-Level Direction

After the 90 days:

- Learning With Rounding
- Module-SIS
- NTRU
- Fourier analysis
- Discrete Gaussian sampling
- Lattice reduction
- LLL
- BKZ
- Cryptographic reductions
- Security proofs
- Concrete security estimates
- Side-channel resistant implementation
- Fault resistance
- Formal verification

---

# What NOT to Do During the First 90 Days

### Don't start with quantum mechanics textbooks.

You need quantum computing concepts, but PQC is not primarily quantum physics.

### Don't start by implementing ML-KEM from scratch.

First understand:
`modular arithmetic → polynomials → lattices → LWE → Module-LWE → KEM`

### Don't memorize standards.

Learn how to read them.

### Don't trust "unbreakable" claims.

Cryptography is about assumptions, models, parameters, reductions, implementations, and attack costs.

### Don't use toy cryptography in real systems.

Toy implementations are for learning.

---

# The Long-Term Roadmap After Day 90

Your 90 days are only **Level 1**.

## Level 2 — Cryptography Engineer

Study:

- Applied cryptographic libraries
- TLS
- PKI
- KEM APIs
- Digital signature APIs
- Hardware security
- Secure coding
- Protocol engineering

Build:

- PQC-enabled client/server
- Crypto-agile protocol
- PQC certificate experiment

---

## Level 3 — Mathematical Cryptography

Study deeply:

- Abstract algebra
- Probability
- Number theory
- Finite fields
- Lattice theory
- Complexity theory

Read:

- Textbooks
- Survey papers
- NIST standards
- Original algorithm papers

---

## Level 4 — PQC Research

Study:

- Lattice reductions
- Security proofs
- Attack algorithms
- Parameter selection
- Cryptanalysis
- Side channels
- Implementation attacks

Start reproducing experiments from papers.

---

## Level 5 — Researcher

Eventually:

```text
Read a paper
     ↓
Understand the assumption
     ↓
Understand the proof
     ↓
Implement the construction
     ↓
Implement/reproduce an attack
     ↓
Benchmark it
     ↓
Find an open problem
     ↓
Propose/test an idea
```

That is the path from **learning PQC** to **doing PQC research**.

---

# Final 90-Day Milestone

At the end, you should have:

- [ ] 90 daily learning logs
- [ ] 5–6 substantial projects
- [ ] Number theory toolkit
- [ ] Classical cryptography lab
- [ ] Quantum simulator
- [ ] LWE laboratory
- [ ] Lattice visualizer
- [ ] PQC secure-messaging prototype
- [ ] Threat model
- [ ] Security review
- [ ] Notes on ML-KEM
- [ ] Notes on ML-DSA
- [ ] Notes on SLH-DSA
- [ ] Final PQC report
- [ ] GitHub repository documenting the journey

## The most important principle

Do not measure the 90 days by:

> "How many topics did I finish?"

Measure them by:

> **"How many concepts can I explain, derive, implement, test, and attack?"**

That mindset will take you much further than simply completing a course.

---

## Official references to keep bookmarked

- NIST Post-Quantum Cryptography: https://csrc.nist.gov/projects/post-quantum-cryptography
- NIST PQC standards: https://csrc.nist.gov/Projects/Post-Quantum-Cryptography/Post_Quantum_Cryptography-Standardization
- FIPS 203 / ML-KEM
- FIPS 204 / ML-DSA
- FIPS 205 / SLH-DSA
- NIST PQC publications: https://csrc.nist.gov/Projects/post-quantum-cryptography/publications

**Roadmap version:** September 2026
