import  React, { useState } from  'react';
import  DiaryService  from  '../DiaryService';
import showdown from 'showdown';
import { useParams } from 'react-router';

const  diaryService  =  new  DiaryService();

export default function SinglePost() {
    let { id } = useParams();
    let converter = new showdown.Converter(),
        [content_processed, setContent] = useState(),
        [title, setTitle] = useState();
    diaryService.getPost(id).then(response => {
        setTitle(response.title);
        setContent(converter.makeHtml(response.content));
    })
    return (
        <div>
            <h1>{title}</h1>
            <div className='post-md' dangerouslySetInnerHTML={{__html:content_processed}} />
        </div>
    )

}
