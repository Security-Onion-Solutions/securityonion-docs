.. _getting-started:

Getting Started
===============

If you're ready to get started with Security Onion, you may have questions like:

**What are the recommended best practices?**

See the :ref:`best-practices` section.

**How many machines do I need?**

Depending on what you're trying to do, you may need anywhere from one machine to thousands of machines. The :ref:`architecture` section will help you decide.

**What kind of hardware does each of those machines need?**

This could be anything from a small virtual machine to a large rack mount server with lots of CPU cores, lots of RAM, and lots of storage. The :ref:`hardware` section provides further details.

**Which ISO image should I download?**

You can download our Security Onion ISO image or a standard 64-bit Rocky Linux 9 or Ubuntu 22.04 ISO image. We recommend our Security Onion ISO image for most use cases, but you should review the :ref:`partitioning`, :ref:`release-notes`, and :ref:`download` sections for more information.

**If I just want to try Security Onion in a virtual machine, how do I create a virtual machine?**

See the :ref:`vmware` and :ref:`virtualbox` sections.

**How do I deploy Security Onion in the cloud?**

See the :ref:`cloud-ami` and :ref:`cloud-azure` sections.

**What if I have trouble booting the ISO image?**

Check out the :ref:`trouble-booting` section.

**What if I'm on an airgap network?**

Review the :ref:`airgap` section.

**Once I've booted the ISO image, how do I install it?**

The :ref:`installation` section has steps for our Security Onion ISO image and for standard Rocky Linux 9 and Ubuntu 22.04 ISO images.

**After installation, how do I configure Security Onion?**

The :ref:`configuration` section covers many different use cases.

**Is there anything I need to do after configuration?**

See the :ref:`post-installation` section.

.. toctree::
   :maxdepth: 2

   best-practices
   architecture
   hardware
   partitioning
   download
   vmware
   virtualbox
   proxmox
   trouble-booting
   airgap
   installation
   cloud-ami
   cloud-azure
   configuration
   post-installation
