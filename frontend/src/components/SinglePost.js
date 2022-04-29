import  React, { useState } from  'react';
import  DiaryService  from  '../DiaryService';
import showdown from 'showdown';
import { useParams } from 'react-router';

const  diaryService  =  new  DiaryService();

export default function SinglePost() {
    let { id } = useParams();
    let converter = new showdown.Converter(),
        [htmlStore, setHtml] = useState();
    diaryService.getPost(id).then(response => {
        setHtml(converter.makeHtml(response.content));
        console.log(htmlStore);
    })
    return (
        <div>
            <div className='post-md' dangerouslySetInnerHTML={{__html:htmlStore}} />
        </div>
    )

}
