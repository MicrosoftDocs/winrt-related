---

ms.assetid: 948fbf9b-c4c8-42d6-8659-04392d3c13f2
title: desktop2:TypeSupported
description: Specifies the types of events that are supported.

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:TypeSupported


## Description
Specifies the types of events that are supported.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop2-package-extension.md">&lt;desktop2:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop2-DesktopEventLogging.md">&lt;desktop2:DesktopEventLogging&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop2-typessupported.md">&lt;desktop2:TypesSupported&gt;</a></dt>
<dd><b>&lt;desktop2:TypeSupported&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax
```syntax
<desktop2:TypeSupported Value = A string value that specifies the type of event logging. See the Attributes table for more info. >
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Value | The value of event log types supported. | One of the following string values: <ul><li>EVENTLOG_AUDIT_FAILURE</li><li>EVENTLOG_AUDIT_SUCCESS</li><li>EVENTLOG_ERROR_TYPE</li><li>EVENTLOG_INFORMATION_TYPE</li><li>EVENTLOG_WARNING_TYPE</li></ul> | Yes |

## Requirements

|               |       Value                                                      |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |