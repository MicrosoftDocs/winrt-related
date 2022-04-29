---
title: desktop8:Publishing
description: Provides access to the Publishing feature within an Event Tracing channel.
keywords: windows 10, uwp, schema, manifest, desktop
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:Publishing

## Description

Provides access to the Publishing feature within an Event Tracing channel.

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
<dd><strong>&lt;desktop8:Publishing&gt;</strong></dd>
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
<desktop8:Publishing
          Level?       = A byte-type number value.
          Keywords?    = A long-type number value.
          ControlGuid? = A hexadecimal string that may only contain the following values: 0-9 or A-F (uppercase or lowercase) representing the unique identifier of the provider.
          BufferSize?  = An integer-type number value.
          FileMax?     = An integer-type number value.
          MinBuffers?  = An integer-type number value.
          MaxBuffers?  = An integer-type number value.
          Latency?     = An integer-type number value.
          ClockType?   = Specifies the clock type to be used during publishing. | A string value that can be one of the following: "systemTime" or "queryPerformanceCounter".
          SidType?     = Specifies the security identifier type for publishing. | A string value that can be one of the following: "none", or "publishing".
          >

</desktop8:Publishing>
```

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Level | Specifies the level for publishing. | A byte-type number value. | No |
| Keywords | Specifies the keywords used for publishing. | A long-type number value. | No |
| ControlGuid | Specifies the GUID used for controlling publishing. | A hexadecimal string that may only contain the following values: 0-9 or A-F (uppercase or lowercase) representing the unique identifier of the provider. | No |
| BufferSize | Specifies the buffer size during publishing. | An integer-type number value. | No |
| FileMax | Specifies the maximum file size for publishing. | An integer-type number value. | No |
| MinBuffers | Specifies the minimum buffer size during publshing. | An integer-type number value. | No |
| MaxBuffers | Specifies the maximum buffer size during publishing. | An interger-type number value. | No |
| Latency | Specifies the latency to accept when publishing. | An integer-type number value. | No |
| ClockType | Specifies the clock type to be used during publishing. | A string value that can be one of the following: "systemTime" or "queryPerformanceCounter". | No |
| SidType | Specifies the security identifier type for publishing. | A string value that can be one of the following: "none", or "publishing". | No |

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