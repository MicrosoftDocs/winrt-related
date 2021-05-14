---

title: uap3:Verb
description: Defines the verbs associated with a file context menu.

ms.date: 11/26/2019
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap3:Verb

## Description
Defines the verbs associated with a file context menu and enables Windows Desktop Bridge apps to use ddeexec to launch.

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
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap-extension.md">&lt;uap:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap-FileTypeAssociation.md">&lt;uap:FileTypeAssociation&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap2-supportedverbs.md">&lt;uap2:SupportedVerbs&gt;</a></dt>
<dd><b>&lt;uap2:Verb&gt;</b></dd>
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
```syntax
<uap2:Verb Id = An alphanumeric string between 3 and 64 characters in length.
           Extended? = Boolean.
           rescap3:DdeExecCommand? = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
           rescap3:DdeExecApplication? = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
           rescap3:DdeExecTopic? = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
           rescap3:DdeExecIfExec? = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
           uap7:Default? = boolean value.
           uap3:Parameters? = A string that contains one or more app parameters.
           uap3:MultiSelectModel = One of the following strings: Player, Document, or Single. >
```    

### Key
`?` optional (zero or one)

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Id | The name of the verb. | An alphanumeric string between 3 and 64 characters in length. | Yes |
| Extended | Specifies that the verb should only appear if the user holds the **Shift** key before right-clicking the file to show the context menu. | Boolean. | No |
| rescap3:DdeExecCommand | A DDE command string. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |
| rescap3:DdeExecApplication | An application name used to establish the DDE conversion. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |
| rescap3:DdeExecTopic | The topic name of the DDE conversion. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |
| rescap3:DdeExecIfExec | The DDE command used if DDE conversion cannot be executed. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |
| uap7:Default | Specifies whether the verb is the default verb. | A boolean value. | No |
| uap3:Parameters | Specifies the parameters for the app. | A string that contains one or more app parameters. | No |
| uap3:MultiSelectModel | Specifies the activation model for apps that are started when the user selects and opens multiple files at the same time. For more information, see [this article](/windows/apps/desktop/modernize/desktop-to-uwp-extensions#define-how-your-application-behaves-when-users-select-and-open-multiple-files-at-the-same-time). | One of the following strings: Player, Document, or Single. | No |

## Requirements

|   | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |