---
title: desktop8:Channel
description: Specifies a channel to be used for event tracing.
keywords: windows 10, uwp, schema, manifest, desktop
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:Channel

## Description

Specifies a channel to be used for event tracing.

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
<dd><strong>&lt;desktop8:Channel&gt;</strong></dd>
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
<desktop8:Channel
          Name      = A string with a value between 1 and 2,084 characters.
          Type      = A string value that can be one of the following: "admin", "operational", "analytic", or "debug"
          Access    = The access level of the channel.
          Isolation = Specifies the channels isolation attribute.
          Enabled   = Specifies whether or not the channel is enabled.
          >

  <!-- Child Elements -->
  desktop8:Logging
  desktop8:Publishing

</desktop8:Channel>
```

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name | The name of the channel. | A string with a value between 1 and 2,084 characters. | Yes |
| Type | The type of the channel. | A string value that can be one of the following: "admin", "operational", "analytic", or "debug" | Yes |
| Access | The access level of the channel. | An alphanumeric string. | No |
| Isolation | Specifies the channel's isolation attribute. | A string value that can be one of the following: "application", "system", or "custom" | No |
| Enabled | Specifies whether or not the channel is enabled. | A boolean value. Defaults to false. | No |

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop8:Logging](element-desktop8-logging.md) | Provides access to the Logging feature within an Event Tracing channel. |
| [desktop8:Publishing](element-desktop8-publishing.md) | Provides access to the Publishing feature within an Event Tracing channel. |

### Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [desktop8:Channels](element-desktop8-channels.md) | Allows one or more channels to be specified for event tracing. |

## Requirements

| **Namespace** | **Value** |
|---------------|-----------|
| **desktop8** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |