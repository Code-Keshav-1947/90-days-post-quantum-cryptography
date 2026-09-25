# Cryptography Map

## What is Cryptography?

Cryptography is not just about encrypt something that is secret. It will also contain Integrity, Authentication, and Secrecy.

```First_Doubt
Cryptography ≠ Encryption

Cryptography = Encryption + Integrity + Authentication + Secrecy
```

## Types of Cryptography

There are two types of **Cryptography**:

- **Symmetric Cryptography** - In This we have only one key that use for both operation ( Encrypting and Decrypting ) .

```
Alice                         Bob

message                       ciphertext
   │                               │
   ↓                               ↓
 encryption                     decryption
   │                               │
   └────── same secret key ────────┘
```

**Important**

`It is generally very efficient`

`If it has one key it doesn't mean that it is weak it is generally used to encypt bulk data not real time cummunication`

- **Asymmetric Cryptography** - In This we have two keys ( Public and Private ) that are used for encryption and decryption .

```
Public Key can be shared with everyone but Private Key should be kept secret
```

**What this will do as compare to Symmetric ?**

We are facing a problem that was _Sharing the secret key securly_ in this we don't need to make the public key secret bcz it will only used to encrypt the message and the private key will be used to decrypt the message.

## Why Do we need Post Quantum Cryptography ?

With the advent of quantum computing, traditional cryptographic methods may become vulnerable. Post Quantum Cryptography aims to develop algorithms that are secure against both classical and quantum computers.

**If a quantum Computer is running shor algorithm it will break the classical encryption**

`So we need post quantum cryptography`
