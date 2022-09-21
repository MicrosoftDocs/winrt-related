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

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap12:Extension\>](element-uap12-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**<\uap12:Host\>**

## Syntax

```xml
<uap12:Host
  Name = 'An alphanumeric string with a value between 1 and 255 characters that can contain the following characters: ., -, or *. No other characters are accepted. Represents the domain name with an asterisk ("*") signifying a subdomain.'
  Uri = 'An alphanumeric string with a value between 1 and 255 characters that can contain the following characters: ., -, or *. No other characters are accepted. Represents the domain name with an asterisk ("*") signifying a subdomain.'
  uap11:path = 'An optional alphanumeric string with a value between 1 and 2084 characters that also accepts the following characters: "/", or "\". No other characters are accepted. Represents the path to the domain and/or subdomain.' />
```

### Key

`?`  optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required |
|-|-|-|:-:|
| **Name** | Represents the domain name with the star signifying a subdomain. | An alphanumeric string with a value between 1 and 255 characters that can contain the following characters: ., -, or *. No other characters are accepted. Represents the domain name with an asterisk ("*") signifying a subdomain. | Yes |
| **Uri** | Represents the URI for the domain name with the star signifying a subdomain. | An alphanumeric string with a value between 1 and 255 characters that can contain the following characters: ., -, or *. No other characters are accepted. Represents the domain name with an asterisk ("*") signifying a subdomain. | Yes |
| **uap11:Path** | Represents the path to the domain and/or subdomain. | An optional alphanumeric string with a value between 1 and 2084 characters that also accepts the following characters: "/", or "\". No other characters are accepted. Represents the path to the domain and/or subdomain. | No |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Extension (in Package/Applications)](element-extension.md) | Declares an extensibility point for the app. |

### Requirements

| Item | Value |
|-|-|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows/10/12` |
| **UAP11** | `http://schemas.microsoft.com/appx/manifest/uap/windows/10/11` |
