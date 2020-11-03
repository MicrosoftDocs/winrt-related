---
title: IndexableContent
description: Indicates that the element's text should be indexed for search, but is not associated with a property. 
Search.Product: eADQiWindows 10XVcnh
ms.assetid: 05953531-49EE-4209-9B9D-9A6D465E9772

keywords: windows 10, uwp, schema


ms.topic: reference
ms.date: 04/05/2017
---

# IndexableContent


Indicates that the element's text should be indexed for search, but is not associated with a property. Note that properties can be retrieved later based on the property key, but text content cannot.

``` syntax
<element
    sc:IndexableContent= "true" | "false" | "1" | "0"
    xmlns:sc="http://schemas.microsoft.com/Search/2013/ApplicationContent">
</element>
```

## Data type


This attribute accepts boolean values:

-   `true`
-   `false`
-   `1`
-   `0`

## Examples

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

You can even tell Windows Search to index the content of arbitrary elements. Just use the **IndexableContent** attribute to tell Search to index the content. In the preceding example, Windows Search will index the content of the IndexerSampleSpecificElement because the **IndexableContent** attribute is set to **true**:

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

For the complete code, see the [Indexer sample](/samples/browse/).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 8.1 [desktop apps only]</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2012 R2 [desktop apps only]</p></td>
</tr>
</tbody>
</table>

## See also


[Indexer sample](/samples/browse/)

[**Windows.Storage.Search**](/uwp/api/Windows.Storage.Search)

 

 