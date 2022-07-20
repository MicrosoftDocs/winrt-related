---
title: desktop8:EventTracing
description: Enables your desktop application to log application-defined events to be consumed in real time or saved to a log file.
keywords: windows 10, uwp, schema, manifest, desktop
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:EventTracing

## Description

Enables your desktop application to log application-defined events to be consumed in real time or saved to a log file.

## Element Hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</dt>
<dd>
<dl>
<dt><a href="element-desktop8-extension.md">&lt;desktop8:Extension&gt;</a></dt>
<dd><strong>&lt;desktop8:EventTracing&gt;</strong></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

```xml
<desktop8:EventTracing>

  <!-- Child Elements -->
  desktop8:Provider

</desktop8:EventTracing>
```

## Attributes and Elements

### Attributes

None.

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop8:Provider](element-desktop8-provider.md) | Registers a provider to Event Tracing and enables its functionality. |

### Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [desktop8:Extension (in Package/Application)](element-desktop8-extension.md) | Declares an extensibility point for the application. |

## Requirements

| **Namespace** | **Value** |
|---------------|-----------|
| **desktop8** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |