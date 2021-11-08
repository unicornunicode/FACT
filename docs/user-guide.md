
# User Guide

## Concepts

- Controller: The overall orchestrator of the operations. Keeps a log of what
  the user has done and assigns tasks to workers.
- Workers: Take tasks from the controller. These tasks instruct the worker to
  capture and analyse evidence from targets.
- Targets: Machines that you wish to capture evidence from.

## UI

Once you've [installed](installation.md) FACT, you can open up the UI by opening
[http://localhost:3000](http://localhost:3000) in a web browser to start using
FACT.

### Adding targets

The first thing you might want to do is to add a target. Visit the "Targets"
page to add the targets you wish to capture evidence from into FACT. Give it a
display name for your reference (and later on used in Kibana), and enter the
user, host and port used to connect to the target.

You should add an existing SSH keypair to connect to the target, or generate a
new one and install it on the target. Paste the private key into the box.

When using a non-root user, you should check the "Use sudo" checkbox.

> At the moment, "Use sudo" only works when there is no password prompt
> (`NOPASSWD`) for the user.

### Discovering disks

Before you can collect disks, FACT has to know about them. Select all the
targets you'd like to capture and press "Scan disks". Give it a while to
discover the block devices on every machine.

> Behind the scenes, this runs `lsblk -lb` on each target.

### Capturing disk images

Once the disk discovery has completed, you can pick the disks you wish to
capture. Picking the block device will capture the entire device including all
its partitions. Picking a partition device will capture only the filesystem on
that partition. Once you're done picking, press "Capture disks". This may take
minutes, hours or days depending on the amount of data you are capturing, the
number of workers you have and the disk performance of both the targets and the
workers, amongst other factors.

> Behind the scenes, this runs `dd` on each target and streams the device to
> the worker over SSH.

### Analysing disk images

When disks have been captured, analysis can be started by selecting the devices
and pressing "Ingest captures". This will start the process of ingestion of the
data within the collected disk images. It might take a while too.

### Viewing the data

Once ingestion has completed, open Kibana by visiting [http://localhost:5601](http://localhost:5601/app/discover).

To view a log of events, open the menu and visit "Discover". You might be
prompted to create an index pattern. Create an index pattern `fact-*-files` or
`fact-*` to match all FACT indexes. Optionally, pick one of the file time
attributes (mtime, ctime or atime) as the time field to sort entries by that
attribute.

After your index pattern is created, you can open "Discover" again to view the
log of events, search and sort through them.

For more information on using Kibana, consult its
[official documentation](https://www.elastic.co/guide/en/kibana/7.15/index.html).

<!-- vim: set conceallevel=2 et ts=2 sw=2: -->
