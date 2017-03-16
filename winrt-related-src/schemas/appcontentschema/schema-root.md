---
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
title: Application content schema
description: The Application content schema for UWP apps enables developers to enhance in-app search by providing extra information about your app's content to the Windows Search Index.
author: mcleblanc
ms.author: markl
ms.topic: article
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, schema
---

# Application content schema


The Application content, or appcontent-ms, schema for Windows apps enables developers to enhance in-app search by providing extra information about your app's content to the Windows Search Index.

## How it works


To request that Windows index your app data for in-app searches, create a folder named "Indexed" under the [**LocalFolder**](https://msdn.microsoft.com/library/windows/apps/br241621) and store the files that you want indexed there. Windows indexes the file content and metadata (properties) in this "Indexed" folder and all its subfolders.

To use the appcontent-ms schema to index info about a file or item, create an appcontent-ms file and add it to your app's [**LocalFolder**](https://msdn.microsoft.com/library/windows/apps/br241621)\\Indexed folder (you need to do this at runtime, after your app has been installed). When your app uses [**Windows.Storage.Search**](https://msdn.microsoft.com/library/windows/apps/br208106) APIs to perform queries on the Indexed folder, Search will include information from your appcontent-ms files.

The info in appcontent-ms files is only used when the app that contains them uses the [**Windows.Storage.Search**](https://msdn.microsoft.com/library/windows/apps/br208106) API to performs searches; the info won't show up in Windows UI or in other apps, for example.

This example shows a simple appcontent-ms file that describes an item named "Sample 1".

Notice that the file contains elements not defined by the appcontent-ms schema: `IndexerSampleInformation` and `IndexerSampleSpecificElement`. Your appcontent-ms file must have a root node that encapsulates all the data to be indexed, but you can name that node anything you want.

```XML
<?xml version="1.0" encoding="utf-8"?>
<IndexerSampleInformation>
  <Properties xmlns="http://schemas.microsoft.com/Search/2013/ApplicationContent">
    <Name>Sample 1</Name>
    <Keywords>
      <Keyword xml:lang="en-US">Sample 1 - keyword 1</Keyword>
      <Keyword>Sample 1 - keyword 2</Keyword>
    </Keywords>
    <Comment>Sample 1 comment</Comment>
    <AdditionalProperties>
      <Property Key="System.Title">Sample 1 Title</Property>
      <Property xml:lang="en-US" Key="System.Contact.EmailAddresses">
        <Value>bryan@contoso.com</Value>
        <Value>vincent@contoso.com</Value>
      </Property>
    </AdditionalProperties>
  </Properties>
  <IndexerSampleSpecificElement sc:IndexableContent="true" 
    xmlns:sc="http://schemas.microsoft.com/Search/2013/ApplicationContent">
    The text included here will be indexed, enabling full-text search.
  </IndexerSampleSpecificElement>
</IndexerSampleInformation>
```

You can even tell Windows Search to index the content of arbitrary elements. Just use the [**IndexableContent**](indexablecontent.md) attribute to tell Search to index the content. In the preceding example, Windows Search will index the content of the IndexerSampleSpecificElement because the **IndexableContent** attribute is set to **true**:

```XML
  <IndexerSampleSpecificElement sc:IndexableContent="true" 
    xmlns:sc="http://schemas.microsoft.com/Search/2013/ApplicationContent">
    The text included here will be indexed, enabling full-text search.
  </IndexerSampleSpecificElement>
```

Search will treat the content as text content by default; if the content is base64, use the [**ContentType**](contenttype.md) attribute to specify the MIME type.

The next example shows how to copy an appcontent-ms file to your app's LocalFolder\\Indexed folder. The code copies any files it finds in the app's appcontent-ms folder to the LocalFolder\\Indexed folder. (You can also create new appcontent-ms files directly in the Indexed folder rather than copying them from another location.)

```CSharp
/// <summary>
/// For the purposes of this sample, the appcontent-ms files are stored in an "appcontent-ms" folder in the
/// install directory. These are then copied into the app&#39;s "LocalState\Indexed" folder, which exposes them
/// to the indexer.
/// </summary>
public async static Task<string> AddAppContentFilesToIndexedFolder()
{
    var localFolder = Windows.Storage.ApplicationData.Current.LocalFolder;
    var installDirectory = Windows.ApplicationModel.Package.Current.InstalledLocation;
    var outputString = "Items added to the \"Indexed\" folder:";
    var appContentFolder = await installDirectory.GetFolderAsync("appcontent-ms");
    var indexedFolder = await localFolder.CreateFolderAsync(
        "Indexed", Windows.Storage.CreationCollisionOption.OpenIfExists);
    var files = await appContentFolder.GetFilesAsync();
    foreach (var file in files)
    {
        outputString += "\n" + file.DisplayName + file.FileType;
        await file.CopyAsync(indexedFolder, 
            file.Name, Windows.Storage.NameCollisionOption.ReplaceExisting);
    }
    return outputString;
}
```

```JavaScript
// For the purposes of this sample, the appcontent-ms files are stored in an "appcontent-ms" folder
// in the install directory.  These are then copied into the app&#39;s "LocalState\Indexed" folder,
// which exposes them to the indexer.
function _addAppContentFilesToIndexedFolder() {
    var localFolder = appData.localFolder,
        appcontentFolder,
        indexedFolder,
        installDirectory = Windows.ApplicationModel.Package.current.installedLocation;
    var output = "Items added to the \"Indexed\" folder:\n";
    installDirectory.getFolderAsync("appcontent-ms").then(function (retrievedAppcontentFolder) {
        appcontentFolder = retrievedAppcontentFolder;
        return localFolder.createFolderAsync(
            "Indexed", Windows.Storage.CreationCollisionOption.openIfExists);
    }).then(function (retrievedIndexedFolder) {
        indexedFolder = retrievedIndexedFolder;
        return appcontentFolder.getFilesAsync(appcontentFolder);
    }).then(function (files) {
        var promiseArray = [];
        for (var i = 0, len = files.length; i < len; i++) {
            promiseArray[i] = files[i].copyAsync(indexedFolder, 
                files[i].name, Windows.Storage.NameCollisionOption.replaceExisting);
            output += files[i].displayName + files[i].fileType;
            if (i < len - 1) {
                output += "\n";
            }
        }
        return WinJS.Promise.join(promiseArray);
    }).done(function () {
        WinJS.log &amp;&amp; WinJS.log(output, "sample", "status");
    });
}
```

For the complete code, see the [Indexer sample](http://go.microsoft.com/fwlink/p/?LinkID=311565).

## Element reference


The following table lists all of the elements in this schema, sorted alphabetically by name.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[AdditionalProperties](element-additionalproperties.md)</td>
<td><p>Contains additional properties that describe the item.</p></td>
</tr>
<tr class="even">
<td>[Comment](element-comment.md)</td>
<td><p>Contains a [System.Comment](https://msdn.microsoft.com/library/windows/desktop/bb760658) that describes the item.</p></td>
</tr>
<tr class="odd">
<td>[Keyword](element-keyword.md)</td>
<td><p>A one of the [System.Keywords](https://msdn.microsoft.com/library/windows/desktop/bb787519) that describes the item.</p></td>
</tr>
<tr class="even">
<td>[Keywords](element-keywords.md)</td>
<td><p>Contains the [System.Keywords](https://msdn.microsoft.com/library/windows/desktop/bb787519) that describe the item.</p></td>
</tr>
<tr class="odd">
<td>[Name](element-name.md)</td>
<td><p>Specifies the [System.ItemName](https://msdn.microsoft.com/library/windows/desktop/bb760768)\[System.ItemNameDisplay](https://msdn.microsoft.com/library/windows/desktop/bb760770) of the item.</p></td>
</tr>
<tr class="even">
<td>[Properties](element-properties.md)</td>
<td><p>Contains properties that describe the item to the Windows Search Index.</p></td>
</tr>
<tr class="odd">
<td>[Property](element-property.md)</td>
<td><p>A property that describes the item.</p></td>
</tr>
<tr class="even">
<td>[Value](element-value.md)</td>
<td><p>The value that will be indexed for the property.</p></td>
</tr>
</tbody>
</table>

 

## Attributes for app-specific elements


Use these attributes to index content in your own app-specific XML elements.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>ContentType</strong>](contenttype.md)</p></td>
<td><p>Setting this property on an element indicates that the element’s content is treated as a base64 encoding of the specified MIME type / content type and is indexed using the handler for that content type.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IndexableContent</strong>](indexablecontent.md)</p></td>
<td><p>Indicates that the element's text should be indexed for search, but is not associated with a property. Note that properties can be retrieved later based on the property key, but text content cannot.</p></td>
</tr>
</tbody>
</table>

 

## Related topics


[Indexer sample](http://go.microsoft.com/fwlink/p/?LinkID=311565)

[**Windows.Storage.Search**](https://msdn.microsoft.com/library/windows/apps/br208106)

[Adding search (HTML)](https://msdn.microsoft.com/library/windows/apps/hh465231)

[Adding search (XAML)](https://msdn.microsoft.com/library/windows/apps/xaml/jj130767)

 

 



