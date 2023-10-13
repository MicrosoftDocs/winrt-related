---
title: uap17:UpdateWhileInUse
description: TBD
ms.date: 10/12/2023
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# uap17:UpdateWhileInUse



## Description

Specifies whether the OS should close the app for app updates, or if the update should be deferred until until the next time the app is restarted by the user or a system reboot. The OS will still force-close the app for required OS updates and system reboots.

## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dd><b>&lt;uap17:UpdateWhileInUse&gt;</b></dd></dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<uap17:UpdateWhileInUse>"allow" | "defer"
</uap17:UpdateWhileInUse>
```





## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| uap17 | http://schemas.microsoft.com/appx/manifest/uap/windows10/17 |
