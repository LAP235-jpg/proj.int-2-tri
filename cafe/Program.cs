using System;
using System.IO.Ports;
using System.Threading;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace MeuPrograma
{
    class Program
    {
        static HttpClient client = new HttpClient();

        static SerialPort stm32 = new SerialPort("COM4", 115200);

        static async Task Main(string[] args)
        {
            stm32.Open();

            Console.WriteLine("STM32 conectado!");

            string buffer = "";

            while (true)
            {
                if (stm32.BytesToRead > 0)
                {
                    buffer += stm32.ReadExisting();

                    while (buffer.Contains("\r\n"))
                    {
                        int fim = buffer.IndexOf("\r\n");

                        string mensagem = buffer.Substring(0, fim);

                        buffer = buffer.Substring(fim + 2);

                        Console.WriteLine($"Recebido: {mensagem}");

                        await ProcessarPacote(mensagem);
                    }
                }

                Thread.Sleep(100);
            }
        }


        static async Task ProcessarPacote(string mensagem)
        {
            if (!mensagem.StartsWith("<CQM|") || !mensagem.EndsWith(">"))
            {
                Console.WriteLine("Pacote inválido!");
                return;
            }

            string conteudo = mensagem.Substring(5, mensagem.Length - 6);

            string[] partes = conteudo.Split('|');

            if (partes.Length != 2)
            {
                Console.WriteLine("Formato inválido!");
                return;
            }

            string temperaturaTexto = partes[0].Replace("T=", "");
            string checksumRecebido = partes[1].Replace("X=", "");

            if (!int.TryParse(temperaturaTexto, out int temperatura))
            {
                Console.WriteLine("Temperatura inválida!");
                return;
            }

            byte checksumCalculado = XorChecksum(
                $"<CQM|T={temperatura}>"
            );

            string checksumCalculadoTexto =
                checksumCalculado.ToString("X2");

            Console.WriteLine($"Temperatura: {temperatura}");
            Console.WriteLine($"X recebido: {checksumRecebido}");
            Console.WriteLine($"X calculado: {checksumCalculadoTexto}");

            if (checksumRecebido.Equals(
                checksumCalculadoTexto,
                StringComparison.OrdinalIgnoreCase))
            {
                Console.WriteLine("Pacote válido!");

                // Valores utilizados pela IA
                string moagem = "Media";
                string torra = "Media";

                await EnviarDados(temperatura, moagem, torra);
            }
            else
            {
                Console.WriteLine("Checksum inválido!");
            }
        }


        static async Task EnviarDados(
            int temperatura,
            string moagem,
            string torra)
        {
            var dados = new
            {
                temperatura = temperatura,
                moagem = moagem,
                torra = torra
            };

            string json = JsonSerializer.Serialize(dados);

            Console.WriteLine($"Enviando para Flask: {json}");

            StringContent conteudo = new StringContent(
                json,
                Encoding.UTF8,
                "application/json"
            );

            try
            {
                HttpResponseMessage resposta = await client.PostAsync(
                    "http://127.0.0.1:5000/temperatura",
                    conteudo
                );

                string retorno =
                    await resposta.Content.ReadAsStringAsync();

                Console.WriteLine(
                    $"Resposta do Flask: {retorno}"
                );
            }
            catch (Exception erro)
            {
                Console.WriteLine(
                    $"Erro ao enviar para o Flask: {erro.Message}"
                );
            }
        }


        static byte XorChecksum(string dados)
        {
            byte checksum = 0;

            foreach (char caractere in dados)
            {
                checksum ^= (byte)caractere;
            }

            return checksum;
        }
    }
}