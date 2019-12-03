package com.example;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/Search")
public class Search extends HttpServlet {
	
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		String search = request.getParameter("search");
		if (search.equals("신선초")) {
			response.sendRedirect("pages/Angelica.html");
			System.out.println(search);
		}else if(search.equals("알타리무")){
			response.sendRedirect("pages/full-width.html");
			System.out.println(search);
		}else if(search.equals("두릅")){
			response.sendRedirect("pages/Araliaelata.html");
			System.out.println(search);
		}else if(search.equals("아스파라거스")){
			response.sendRedirect("pages/Asparagus.html");
			System.out.println(search);
		}else if(search.equals("콩나물")){
			response.sendRedirect("pages/sidebar-right.html");
			System.out.println(search);
		}else if(search.equals("배추")){
			response.sendRedirect("pages/basic-grid.html");
			System.out.println(search);
		}else if(search.equals("부추")){
			response.sendRedirect("pages/Chives.html");
			System.out.println(search);
		}else if(search.equals("옥수수")){
			response.sendRedirect("pages/corn.html");
			System.out.println(search);
		}else if(search.equals("무화과")){
			response.sendRedirect("pages/Fig.html");
			System.out.println(search);
		}else if(search.equals("파")){
			response.sendRedirect("pages/Greenonion.html");
			System.out.println(search);
		}else if(search.equals("상추")){
			response.sendRedirect("pages/Lettuce.html");
			System.out.println(search);
		}else if(search.equals("연근")){
			response.sendRedirect("pages/lotusroot.html");
			System.out.println(search);
		}else if(search.equals("곰취")){
			response.sendRedirect("pages/Gomchwi.html");
			System.out.println(search);
		}else if(search.equals("청경채")){
			response.sendRedirect("pages/PakChoi.html");
			System.out.println(search);
		}else if(search.equals("완두콩")){
			response.sendRedirect("pages/Pea.html");
			System.out.println(search);
		}else if(search.equals("고구마")){
			response.sendRedirect("pages/Sweetpotato.html");
			System.out.println(search);
		}else if(search.equals("토마토")){
			response.sendRedirect("pages/width.html");
			System.out.println(search);
		}else if(search.equals("수박")){
			response.sendRedirect("pages/sidebar-left.html");
			System.out.println(search);
		}else if(search.equals("호박")){
			response.sendRedirect("pages/pumpkin.html");
			System.out.println(search);
		}else if(search.equals("포도")){
			response.sendRedirect("pages/grape.html");
			System.out.println(search);
		}else {
			response.sendRedirect("F.html");
		}
	}
}
