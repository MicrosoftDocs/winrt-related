---
title: desktop8:Provider
description: Registers a provider to Event Tracing and enables its functionality.
keywords: windows 10, uwp, schema, manifest, desktop
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:Provider

## Description

Registers a provider to Event Tracing and enables its functionality.

## Element Hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</dt>
<dd>
<dl>
<dt><a href="element-desktop8-extension.md">&lt;desktop8:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop8-eventtracing.md">&lt;desktop8:EventTracing&gt;</a></dt>
<dd><strong>&lt;desktop8:Provider&gt;</strong></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

```xml
<desktop8:Provider
          Id           = A hexadecimal string that may only contain the following values: 0-9 or A-F (uppercase or lowercase) representing the unique identifier of the provider.
          Name         = A string value between 1 and 2084 characters in length that represents the name of the provider.
          ResourceFile = A string value where the first character cannot contain any of the following: ".", "/", "\", or a space. Represents the path to a file.
          MessageFile  = A string value where the first character cannot contain any of the following: ".", "/", "\", or a space. Represents the path to a file.
          >

  <!-- Child Elements -->
  desktop8:Channels

</desktop8:Provider>
```

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Id | The unique identifier for the provider. | A hexadecimal string that may only contain the following values: 0-9 or A-F (uppercase or lowercase) representing the unique identifier of the provider. | Yes |
| Name | The name of the provider. | A string value between 1 and 2084 characters in length that represents the name of the provider. | Yes |
| ResourceFile | Specifies the path to the provider resource files. | A string value where the first character cannot contain any of the following: ".", "/", "\", or a space. Represents the path to a file. | Yes |
| MessageFile | Specifies the path to the provider message files. | A string value where the first character cannot contain any of the following: ".", "/", "\", or a space. Represents the path to a file. | No |

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop8:Channels](element-desktop8-channels.md) | Allows one or more channels to be specified for event tracing. |

### Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [desktop8:EventTracing](element-desktop8-eventtracing.md) | Enables your desktop application to log application-defined events to be consumed in real time or saved to a log file. |

## Requirements

| **Namespace** | **Value** |
|---------------|-----------|
| **desktop8** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |