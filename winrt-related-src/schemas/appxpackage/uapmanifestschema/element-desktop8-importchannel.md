---
title: desktop8:ImportChannel
description: Specifies an imported channel to be used for event tracing.
keywords: windows 10, uwp, schema, manifest, desktop
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:ImportChannel

## Description

Specifies an imported channel to be used for event tracing.

## Element Hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop8-extension.md">&lt;desktop8:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop8-eventtracing.md">&lt;desktop8:EventTracing&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop8-provider.md">&lt;desktop8:Provider&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop8-channels.md">&lt;desktop8:Channels&gt;</a></dt>
<dd><strong>&lt;desktop8:ImportChannel&gt;</strong></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
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

```xml
<desktop8:ImportChannel
          Name = A string with a value between 1 and 2,084 characters.
          >

</desktop8:ImportChannel>
```

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name | The name of the channel. | A string with a value between 1 and 2,084 characters. | Yes |

### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [desktop8:Channels](element-desktop8-channels.md) | Allows one or more channels to be specified for event tracing. |

## Requirements

| **Namespace** | **Value** |
|---------------|-----------|
| **desktop8** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |