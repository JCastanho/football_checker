package com.jcastanho;

import java.io.IOException;
import java.util.List;

import com.gargoylesoftware.htmlunit.*;
import com.gargoylesoftware.htmlunit.html.*;
import com.gargoylesoftware.htmlunit.javascript.host.dom.NodeList;

import org.w3c.dom.Node;





public class App 
{

    // public static Iterable<DomNode> getTeams(Iterable<DomNode> list){
    //     Iterable<DomNode> children = new Iterable<DomNode>();
    //     if(list. == 0){
    //         return list;
    //     }else if(list.getLength() > 0){
    //         for(int i = 0; i < list.getLength();i++){
    //             Node child = list.item(i);
    //             System.out.println(child);
    //             children.add(child.getChildNodes());
    //         }
    //     }
    //     return getTeams(children);
    // }
    public static void main( String[] args )
    {
        // String url = "https://www.sofascore.com/pt/time/futebol/sl-benfica/3006";
        String url = "https://www.sofascore.com/pt/torneio/futebol/portugal/primeira-liga/238";
        // String url ="https://desporto.sapo.pt/futebol/competicao/primeira-liga-2/classificacao";

        WebClient webClient = new WebClient(BrowserVersion.CHROME);
        webClient.waitForBackgroundJavaScript(50000);
        webClient.getOptions().setUseInsecureSSL(true);
        webClient.getOptions().setCssEnabled(false);
        webClient.getOptions().setJavaScriptEnabled(false);
        try{
            HtmlPage htmlPage = webClient.getPage(url);
            List<HtmlDivision> divs = htmlPage.getByXPath("//div");
            List<HtmlDivision> tab_header = htmlPage.getByXPath("//div[contains(@class, 'Content__PageContainer-sc-g01dez-0 eyhylD')]");
            Iterable<DomNode> children = tab_header.get(0).getDescendants();
            // Iterable<DomNode> teste = getTeams(children);
            List<HtmlDivision> tab_content = htmlPage.getByXPath("//div[@class='content']");
            for (DomNode element : children){
                // System.out.println(element);
                System.out.println(element.getTextContent());
            }
            // for(HtmlDivision element : tab_header){
            //     System.out.println(element);
            //     System.out.println(element.getTextContent());
            // }
            // for(int index = 0; index < children.getLength(); index++){
            //     Node child = children.item(index);
            //     System.out.println(child);
            // }
        }catch (Exception e){
            System.out.println("Deu Merda!");
        }
        
        
    }
}
