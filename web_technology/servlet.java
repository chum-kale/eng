import java.sql.*;
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
/**
*
* @author mmcoe
*/
public class NewServletTC2214 extends HttpServlet
{						   /**
* Processes requests for both HTTP <code>GET</code> and <code>POST</code>
* methods.
*
* @param request servlet request
* @param response servlet response
* @throws ServletException if a servlet-specific error occurs
* @throws IOException if an I/O error occurs
*/
  protected void processRequest (HttpServletRequest request,
				 HttpServletResponse response) throws
    ServletException, IOException
  {
    response.setContentType ("text/html;charset=UTF-8");
    PrintWriter out = response.getWriter ();
      try
    {
      Class.forName ("com.mysql.jdbc.Driver");
      Connection conn =
	DriverManager.getConnection ("jdbc:mysql://localhost:3306/WT", "root",
				     "mmcoe");
        out.println ("<html><body>");
        out.println ("<table border=1 width=50% height=50%>");
        out.println
	("<tr><th>id</th><th>title</th><th>author</th><th>price</th><th>quantity</th><tr>");
      Statement stmt = conn.createStatement ();
      ResultSet rs = stmt.executeQuery ("Select * from ebookshop");
      while (rs.next ())
	{
	  int n = rs.getInt ("id");
	  String nm = rs.getString ("title");
	  String am = rs.getString ("author");
	  int s = rs.getInt ("price");
	  int quant = rs.getInt ("quantity");
	    out.println ("<tr><td>" + n + "</td><td>" + nm + "</td><td>" +
			 am + "</td><td>" + s + "</td><td>" + quant +
			 "</td></tr>");
	}
      out.println ("</table>");
      out.println ("</html></body>");
      conn.close ();
    } catch (Exception e)
    {
      out.println ("<h1>Error</h1>");
    }				//
//
    out.println ("</body>");
    out.println ("</html>");
  }
<editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the
  left to edit the code.">

/**
* Handles the HTTP <code>GET</code> method.
*
* @param request servlet request
* @param response servlet response
* @throws ServletException if a servlet-specific error occurs
* @throws IOException if an I/O error occurs
*/
@Override
protected void doGet(HttpServletRequest request, HttpServletResponse response)
throws ServletException, IOException {
processRequest(request, response);
}
/**
* Handles the HTTP <code>POST</code> method.
*
* @param request servlet request
* @param response servlet response
* @throws ServletException if a servlet-specific error occurs
* @throws IOException if an I/O error occurs
*/
@Override
protected void doPost(HttpServletRequest request, HttpServletResponse response)
throws ServletException, IOException {
processRequest(request, response);
}
/**
* Returns a short description of the servlet.
*
* @return a String containing servlet description
*/
@Override
public String getServletInfo() {
return " Short description ";
}// </editor-fold>
}