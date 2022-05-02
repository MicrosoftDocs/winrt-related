---
title: desktop8:Logging
description: Provides access to the Logging feature within an Event Tracing channel.
keywords: windows 10, uwp, schema, manifest, desktop
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:Logging

## Description

Provides access to the Logging feature within an Event Tracing channel.

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
<dd>
<dl>
<dt><a href="element-desktop8-provider.md">&lt;desktop8:Provider&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop8-channels.md">&lt;desktop8:Channels&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop8-channel.md">&lt;desktop8:Channel&gt;</a></dt>
<dd><strong>&lt;desktop8:Logging&gt;</strong></dd>
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
<desktop8:Logging
          Autobackup? = A boolean value. Specifies whether or not logs should be automatically backed up.
          Retention?  = A boolean value. Specifies whether or not logs should be saved.
          MaxSize?    = A decimal number value specifying the maximum size of the logging file.
          >

</desktop8:Logging>
```

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Autobackup | Specifies whether or not logs should be automatically backed up. | A boolean value. | No |
| Retention | Specifies whether or not logs should be saved. | A boolean value. | No |
| MaxSize | Specifies the maximum size of the logging file. | A decimal number value. | No |

### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [desktop8:Channel](element-desktop8-channel.md) | Specifies a channel to be used for event tracing. |

## Requirements

| **Namespace** | **Value** |
|---------------|-----------|
| **desktop8** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |