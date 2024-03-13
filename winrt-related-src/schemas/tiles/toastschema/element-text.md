---
description: Specifies text used in the toast template.
Search.Product: eADQiWindows 10XVcnh
title: text (Toast schema)
ms.assetid: dac874d1-0a30-4d85-a63d-0ddfa88783d1

keywords: windows 10, uwp, schema, toast notifications


ms.topic: reference
ms.date: 04/05/2017
---

# text  (Toast XML Schema)




Specifies text used in the toast template.

## Element hierarchy

<dl>
<dt><a href="element-toast.md">&lt;toast&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-visual.md">&lt;visual&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-binding.md">&lt;binding&gt;</a></dt>
<dd><b>&lt;text&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<text id    = integer
      lang? = string 
      placement? = "attribution"
      hint-callScenarioCenterAlign? = boolean />
```

### Key

`?`   optional (zero or one)

## Attributes and Elements


### Attributes

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
<th>Data type</th>
<th>Required</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>id</strong></td>
<td><p>The text element in the toast template that this text is intended for. If a template has only one text element, then this value is 1. The number of available text positions is based on the template definition.</p></td>
<td>integer</td>
<td>Yes</td>
<td>None</td>
</tr>
<tr class="even">
<td><strong>lang</strong></td>
<td><p>The target locale of the XML payload, specified as a <a href="https://go.microsoft.com/fwlink/p/?linkid=227302">BCP-47 language tags</a>  such as &quot;en-US&quot; or &quot;fr-FR&quot;. The locale specified here overrides any other specified locale in <a href="element-binding.md"><strong>binding</strong></a> or <a href="element-visual.md"><strong>visual</strong></a>. If this value is a literal string, this attribute defaults to the user's UI language. If this value is a string reference, this attribute defaults to the locale chosen by Windows Runtime in resolving the string.</p></td>
<td>string</td>
<td>No</td>
<td>None</td>
</tr>
<tr class="odd">
<td><strong>placement</strong></td>
<td><p>The placement of the text. Introduced in Anniversary Update. If you specify the value "attribution", the text is always displayed at the bottom of your notification, along with your app's identity or the notification's timestamp. On older versions of Windows that don't support attribution text, the text will simply be displayed as another text element (assuming you don't already have the maximum of three text elements). For more information, see <a href="/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts">Toast content</a>.</p></td>
<td>string</td>
<td>No</td>
<td>None</td>
</tr>
<tr class="even">
<td><strong>hint-callScenarioCenterAlign</strong></td>
<td><p>Set to &quot;true&quot; to center the text for incoming call notifications. This value is only used for notifications with with a <strong>scenario</strong> value of "incomingCall"; otherwise, it is ignored. For more information, see <a href="/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts#scenarios">Toast content</a>.</p></li>
</ul></td>
<td>boolean</td>
<td>No</td>
<td>None</td>
</tr>
</tbody>
</table>

 

### Child Elements

None.

### Parent Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parent Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="element-binding.md">binding</a> </td>
<td><p>Specifies the toast template. Note that only one binding element can be included in a toast notification.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The body of the text element can be expressed in two ways:

-   As a literal string; for instance, &lt;text id="1"&gt;Hello world!&lt;/text&gt;.
-   As a string reference, using the "ms-resource" prefix; for instance, &lt;text id="1"&gt; ms-resource:hello&lt;/text&gt;. When using the "ms-resource" prefix, the string identifier is referenced in the app's Resources.resjson (Windows app using JavaScript) or Resources.resw file (C#/C++).

For more information, see [Globalizing your tile: localization, scaling, and accessibility](/previous-versions/windows/apps/hh831183(v=win.10)).

## See also

* [Toast content](/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts)
* [Notifications Visualizer](/windows/apps/design/shell/tiles-and-notifications/notifications-visualizer)



 

 
