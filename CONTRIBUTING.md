# Contributing

We welcome contributions to this project. This is a dual-licensed project:
documentation and educational content use CC BY 4.0, while source code uses
Apache 2.0.

#### Signing Off Your Work

* We require that all contributors "sign-off" on their commits. This certifies that the contribution is your original work, or you have rights to submit it under the same license, or a compatible license.

  * Any contribution which contains commits that are not Signed-Off will not be accepted.

* To sign off on a commit you simply use the `--signoff` (or `-s`) option when committing your changes:
  ```bash
  $ git commit -s -m "Add cool feature."
  ```
  This will append the following to your commit message:
  ```
  Signed-off-by: Your Name <your@email.com>
  ```

  ```
    Developer Certificate of Origin
    Version 1.1

    Copyright (C) 2004, 2006 The Linux Foundation and its contributors.

    Everyone is permitted to copy and distribute verbatim copies of this
    license document, but changing it is not allowed.


    Developer's Certificate of Origin 1.1

    By making a contribution to this project, I certify that:

    (a) The contribution was created in whole or in part by me and I
        have the right to submit it under the open source license
        indicated in the file; or

    (b) The contribution is based upon previous work that, to the best
        of my knowledge, is covered under an appropriate open source
        license and I have the right under that license to submit that
        work with modifications, whether created in whole or in part
        by me, under the same open source license (unless I am
        permitted to submit under a different license), as indicated
        in the file; or

    (c) The contribution was provided directly to me by some other
        person who certified (a), (b) or (c) and I have not modified
        it.

    (d) I understand and agree that this project and the contribution
        are public and that a record of the contribution (including all
        personal information I submit with it, including my sign-off) is
        maintained indefinitely and may be redistributed consistent with
        this project or the open source license(s) involved.
  ```

## Development guidelines

- Keep notebook outputs and execution counts cleared before committing.
- Do not commit downloaded datasets, generated images, model checkpoints, or
  credentials.
- Run the repository validation commands documented in the README.
- Document the creator, source URL, exact license, and modifications for every
  third-party image, dataset, quotation, or code sample.
- Preserve the existing module order and keep shared code in
  course_content/tutorials/utils.

## Licensing of contributions

- Code files and notebook code cells must be contributed under Apache 2.0.
- Documentation and notebook non-code cells must be contributed under
  CC BY 4.0.
- Third-party material retains its original license and must be recorded in
  THIRD_PARTY_NOTICES.md and REUSE.toml where applicable.
