---
title: uap12:Host
description: Declares domain and subdomain parameters for the uap12 extension.
keywords: windows 10, uwp, schema, manifest, extension

ms.date: 05/03/2022
ms.topic: reference
---

# uap12:Host

Declares domain and subdomain parameters for the uap12 extension.

## Element hierarchy

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
<dt><a href="element-extension.md">Extension</a></dt>
<dd><strong>&lt;uap12:Host&gt;</strong></dd>
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

``` XML
<uap12:Host
  Name = An alphanumeric string value between 1 and 255 characters that also accepts the following characters: ".", "-", or "*". No other characters are accepted. Represents the domain name with the star signifying a subdomain.
  Uri = An alphanumeric string value between 1 and 255 characters that also accepts the following characters: ".", "-", or "*". No other characters are accepted. Represents the URI for the domain name with the star signifying a subdomain.
  uap11:path? = An alphanumeric string value between 1 and 2,084 characters that also accepts the following characters: "/", or "\". No other characters are accepted. Represents the path to the domain and/or subdomain.
  >

</uap12:Host>
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required |
|-|-|-|:-:|
| Name | Represents the domain name with the star signifying a subdomain. | An alphanumeric string value between 1 and 255 characters that also accepts the following characters: ".", "-", or "*". No other characters are accepted. | Yes |
| Uri | Represents the URI for the domain name with the star signifying a subdomain. | An alphanumeric string value between 1 and 255 characters that also accepts the following characters: ".", "-", or "*". No other characters are accepted. | Yes |
| uap11:Path | Represents the path to the domain and/or subdomain. | An alphanumeric string value between 1 and 2,084 characters that also accepts the following characters: "/", or "\". No other characters are accepted. | No |

### Child elements

**None.**

### Parent elements

| Parent element | Description |
|-|-|
| [Extension (in Package/Applications)](element-extension.md) | Declares an extensibility point for the app. |

### Requirements

| Namespace | Path |
|-|-|
| **UAP11** | `http://schemas.microsoft.com/appx/manifest/uap/windows/10/11` |
| **UAP12** | `http://schemas.microsoft.com/appx/manifest/uap/windows/10/12` |