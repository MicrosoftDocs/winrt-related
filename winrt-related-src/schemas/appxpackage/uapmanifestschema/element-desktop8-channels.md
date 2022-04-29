---
title: desktop8:Channels
description: Allows one or more channels to be specified for event tracing.
keywords: windows 10, uwp, schema, manifest, desktop
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:Channels

## Description

Allows one or more channels to be specified for event tracing.

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
<dd><strong>&lt;desktop8:Channels&gt;</strong></dd>
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
<desktop8:Channels>

  <!-- Child Elements -->
  desktop8:Channel
  desktop8:ImportChannel

</desktop8:Channels>
```

## Attributes and Elements

### Attributes

None.

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop8:Channel](element-desktop8-channel.md) | Specifies a channel to be used for event tracing. |
| [desktop8:ImportChannel](element-desktop8-importchannel.md) | Specifies an imported channel to be used for event tracing. |

### Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [desktop8:Provider](element-desktop8-provider.md) | Registers a provider to Event Tracing and enables its functionality. |

## Requirements

| **Namespace** | **Value** |
|---------------|-----------|
| **desktop8** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |